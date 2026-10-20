"""Code reviews against the theme codebook and write summary tables.

Usage: python3 analyze.py reviews.jsonl steam-metrics.csv out_dir
"""
import csv, json, os, sys
from collections import defaultdict

import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codebook import PILLAR, THEMES, code  # noqa: E402

REVIEWS, METRICS, OUT = sys.argv[1:4]
os.makedirs(OUT, exist_ok=True)

rows = [json.loads(l) for l in open(REVIEWS)]
df = pd.DataFrame(rows)
df["words"] = df.text.str.split().str.len()
themes = list(THEMES)
coded = df.text.map(code)
for t in themes:
    df[t] = coded.map(lambda s, t=t: t in s)
df["vote"] = df.voted_up.map({True: "positive", False: "negative"})

# Real share of positive reviews per game, used to reweight the 50/50 stratified sample.
pct_pos = {int(r["appid"]): float(r["steam_pct_positive"]) / 100 for r in csv.DictReader(open(METRICS))}

# 1. Sample description
desc = df.groupby(["group", "game", "vote"]).agg(
    n=("id", "size"), median_words=("words", "median"),
    median_playtime_at_review_h=("playtime_at_review_h", "median")).reset_index()
desc.to_csv(f"{OUT}/sample_by_game.csv", index=False)

# 2. Theme prevalence by group and vote (unweighted, within each stratum)
prev = df.groupby(["group", "vote"])[themes].mean().T.round(3)
prev.index.name = "theme"
prev.insert(0, "pillar", [PILLAR[t] for t in prev.index])
prev.to_csv(f"{OUT}/theme_prevalence_by_group_vote.csv")

# 3. Negative-vs-positive lift: how much more often a theme appears in negative reviews.
# "substantive" = reviews of 20+ words, where a theme has room to appear at all.
lift_rows = []
for subset, base in (("all_reviews", df), ("substantive_20plus_words", df[df.words >= 20])):
  for g, sub in list(base.groupby("group")) + [("all", base)]:
    neg, pos = sub[sub.vote == "negative"], sub[sub.vote == "positive"]
    for t in themes:
        pn, pp = neg[t].mean(), pos[t].mean()
        lift_rows.append({"subset": subset, "group": g, "theme": t, "pillar": PILLAR[t],
                          "n_negative": len(neg), "n_positive": len(pos), "share_in_negative": round(pn, 3),
                          "share_in_positive": round(pp, 3),
                          "neg_to_pos_ratio": round(pn / pp, 2) if pp else None})
pd.DataFrame(lift_rows).to_csv(f"{OUT}/theme_negative_positive_ratio.csv", index=False)

# 4. Population-weighted prevalence per game (reweight strata by the game's real % positive)
w_rows = []
for (app, game, group), sub in df.groupby(["appid", "game", "group"]):
    p = pct_pos[app]
    neg, pos = sub[sub.vote == "negative"], sub[sub.vote == "positive"]
    row = {"appid": app, "game": game, "group": group, "steam_pct_positive": round(p * 100, 1)}
    for t in themes:
        row[t] = round(p * pos[t].mean() + (1 - p) * (neg[t].mean() if len(neg) else 0), 3)
    w_rows.append(row)
wdf = pd.DataFrame(w_rows)
wdf.to_csv(f"{OUT}/theme_weighted_prevalence_by_game.csv", index=False)
wdf.groupby("group")[themes].median().T.round(3).to_csv(f"{OUT}/theme_weighted_prevalence_group_median.csv")

# 5. Playtime at review by group and vote
pt = df.groupby(["group", "vote"]).playtime_at_review_h.describe(percentiles=[.25, .5, .75]).round(1)
pt.to_csv(f"{OUT}/playtime_at_review.csv")

# 6. Unsupervised check: TF-IDF + NMF topics, separately for negative and positive reviews
topic_rows = []
for vote in ("negative", "positive"):
    texts = df[(df.vote == vote) & (df.words >= 8)].text
    vec = TfidfVectorizer(max_df=0.4, min_df=20, stop_words="english", ngram_range=(1, 2),
                          token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z']+\b")
    X = vec.fit_transform(texts)
    nmf = NMF(n_components=20, random_state=0, init="nndsvd", max_iter=400).fit(X)
    W = nmf.transform(X)
    dominant = W.argmax(axis=1)
    vocab = vec.get_feature_names_out()
    for k, comp in enumerate(nmf.components_):
        topic_rows.append({"vote": vote, "topic": k, "share_of_reviews": round((dominant == k).mean(), 3),
                           "top_terms": ", ".join(vocab[i] for i in comp.argsort()[::-1][:12])})
pd.DataFrame(topic_rows).sort_values(["vote", "share_of_reviews"], ascending=[True, False]).to_csv(
    f"{OUT}/nmf_topics.csv", index=False)

# Per-review coded output (without full text) for reuse
df[["appid", "game", "group", "id", "vote", "playtime_at_review_h", "words"] + themes].to_csv(
    f"{OUT}/coded_reviews.csv.gz", index=False, compression="gzip")
print(len(df), "reviews coded")
