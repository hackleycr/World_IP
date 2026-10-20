"""Embedding-based ("semantic") theme classifier for the pillar themes.

Each theme is described by a few seed sentences. Every review is split into sentences; a review's
score for a theme is the highest cosine similarity between any of its sentences and any seed.
A review is tagged when its score passes a threshold calibrated on hand-labelled data.

Usage:
  python3 semantic_classify.py score reviews.jsonl out_dir        # embed + score (cached)
  python3 semantic_classify.py evaluate out_dir hand_labels.json   # calibrate on dev, test on test
"""
import json, os, re, sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codebook import code  # noqa: E402

SEEDS = {
    "grind_repetition": [
        "The game is a repetitive grind.", "It becomes tedious and feels like a chore.",
        "You have to grind for hours to make any progress.", "Doing the same thing over and over gets boring.",
        "The game is padded out to waste your time."],
    "progress_loss_devaluation": [
        "I lost all my progress.", "My save file was deleted.", "They nerfed the gear I worked hard for.",
        "Content I paid for was removed from the game.", "An update made my previous effort worthless."],
    "discovery_curiosity": [
        "I loved exploring and discovering secrets.", "Figuring out how everything works is so satisfying.",
        "The mystery kept me curious the whole time.", "That aha moment when it all finally clicks.",
        "Deciphering clues and piecing things together."],
    "learning_curve_opacity": [
        "The game doesn't explain anything.", "I had to read the wiki to understand how to play.",
        "Steep learning curve and confusing mechanics.", "There is no proper tutorial.",
        "I felt lost and had no idea what to do."],
    "creativity_building": [
        "I love building my own base and factory.", "You can create anything you can imagine.",
        "Freedom to design your own solutions.", "Automating production lines is satisfying.",
        "The building system lets you express yourself."],
    "emergence_simulation": [
        "The physics simulation creates crazy interactions.", "Systems interact with each other in unexpected ways.",
        "Every pixel in the world is simulated.", "Fire, water and materials react realistically.",
        "Chaotic emergent moments happen that nobody planned."],
    "permanence_consequence": [
        "Mistakes are permanent and you can't undo them.", "One wrong decision ruins your whole run.",
        "When you die you have to start over from the beginning.",
        "Your actions have lasting consequences on the world.", "You can lock yourself out with no way back."],
    "content_exhaustion": [
        "After a few hours there is nothing left to do.", "The novelty wears off quickly.",
        "Once you finish it there is no reason to keep playing.", "It gets boring after a while.",
        "There is not enough content."],
}
THEMES = list(SEEDS)
MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def sentences(text):
    text = re.sub(r"\[/?[a-z0-9*]+\]", " ", text)
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+|\n+", text)]
    return [p for p in parts if len(p.split()) >= 3][:40] or [text[:500]]


def score(src, out):
    from sentence_transformers import SentenceTransformer
    os.makedirs(out, exist_ok=True)
    df = pd.DataFrame(json.loads(l) for l in open(src))
    df["words"] = df.text.str.split().str.len()
    df = df[(df.words >= 20) & (df.words <= 600)].reset_index(drop=True)
    sents, owner = [], []
    for i, t in enumerate(df.text):
        s = sentences(t)
        sents += s
        owner += [i] * len(s)
    owner = np.array(owner)
    model = SentenceTransformer(MODEL)
    cache = f"{out}/sentence_embeddings.npy"
    if os.path.exists(cache):
        emb = np.load(cache)
    else:
        emb = model.encode(sents, batch_size=128, normalize_embeddings=True, show_progress_bar=True)
        np.save(cache, emb)
    for t in THEMES:
        seed = model.encode(SEEDS[t], normalize_embeddings=True)
        sim = (emb @ seed.T).max(axis=1)
        best = np.full(len(df), -1.0)
        np.maximum.at(best, owner, sim)
        df[t] = best.round(4)
    cols = ["appid", "game", "group", "id", "voted_up", "playtime_at_review_h", "words"] + THEMES
    df[cols].to_csv(f"{out}/semantic_scores.csv.gz", index=False, compression="gzip")
    df[["id", "text"]].to_json(f"{out}/review_text_index.jsonl", orient="records", lines=True)


def prf(pred, gold):
    tp = sum(p and g for p, g in zip(pred, gold))
    fp = sum(p and not g for p, g in zip(pred, gold))
    fn = sum(g and not p for p, g in zip(pred, gold))
    prec = tp / (tp + fp) if tp + fp else float("nan")
    rec = tp / (tp + fn) if tp + fn else float("nan")
    f1 = 2 * prec * rec / (prec + rec) if prec + rec and not np.isnan(prec + rec) else 0.0
    return tp, fp, fn, prec, rec, f1


def evaluate(out, labels_path):
    labels = json.load(open(labels_path))
    sc = pd.read_csv(f"{out}/semantic_scores.csv.gz", dtype={"id": str}).set_index("id")
    text = pd.read_json(f"{out}/review_text_index.jsonl", lines=True, dtype={"id": str}).set_index("id").text

    def rows(split):
        ids = [i for i in labels[split] if i in sc.index]
        return ids, {t: [t in labels[split][i] for i in ids] for t in THEMES}

    # Calibrate one global threshold on dev (maximise micro-F1 over all themes).
    dev_ids, dev_gold = rows("dev")
    best = max(np.arange(0.30, 0.80, 0.01), key=lambda th: prf(
        sum(([sc.loc[i, t] >= th for i in dev_ids] for t in THEMES), []),
        sum((dev_gold[t] for t in THEMES), []))[5])
    test_ids, test_gold = rows("test")
    res = []
    for method in ("codebook", "semantic", "union"):
        all_p, all_g = [], []
        for t in THEMES:
            lex = [t in code(text[i]) for i in test_ids]
            sem = [sc.loc[i, t] >= best for i in test_ids]
            pred = {"codebook": lex, "semantic": sem, "union": [a or b for a, b in zip(lex, sem)]}[method]
            all_p += pred
            all_g += test_gold[t]
            tp, fp, fn, p, r, f = prf(pred, test_gold[t])
            res.append({"method": method, "theme": t, "gold_positives": sum(test_gold[t]), "tp": tp, "fp": fp,
                        "fn": fn, "precision": round(p, 2), "recall": round(r, 2), "f1": round(f, 2)})
        tp, fp, fn, p, r, f = prf(all_p, all_g)
        res.append({"method": method, "theme": "ALL (micro)", "gold_positives": sum(all_g), "tp": tp, "fp": fp,
                    "fn": fn, "precision": round(p, 2), "recall": round(r, 2), "f1": round(f, 2)})
    df = pd.DataFrame(res)
    df.insert(0, "threshold", round(float(best), 2))
    df.to_csv(f"{out}/method_comparison_test.csv", index=False)
    print(df.to_string(index=False))


if __name__ == "__main__":
    {"score": score, "evaluate": evaluate}[sys.argv[1]](*sys.argv[2:])
