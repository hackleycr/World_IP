"""Embedding-based topic model (BERTopic) over substantive Steam reviews (20+ words).

One model over positive and negative reviews together, so each topic's negative share and
game/group mix can be compared directly. Embeddings: sentence-transformers/all-MiniLM-L6-v2.

Usage: python3 bertopic_run.py reviews.jsonl out_dir
"""
import json, os, sys

import numpy as np
import pandas as pd
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)

df = pd.DataFrame(json.loads(l) for l in open(src))
df["words"] = df.text.str.split().str.len()
df = df[(df.words >= 20) & (df.words <= 600)].reset_index(drop=True)
docs = df.text.str.replace(r"\[/?[a-z0-9*]+\]", " ", regex=True).tolist()  # strip Steam BBCode

model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedder = SentenceTransformer(model_name)
cache = f"{out}/embeddings.npy"
if os.path.exists(cache):
    emb = np.load(cache)
else:
    emb = embedder.encode(docs, batch_size=64, show_progress_bar=True)
    np.save(cache, emb)

topic_model = BERTopic(
    embedding_model=embedder,
    umap_model=UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric="cosine", random_state=42),
    hdbscan_model=HDBSCAN(min_cluster_size=60, min_samples=10, metric="euclidean",
                          cluster_selection_method="eom", prediction_data=True),
    vectorizer_model=CountVectorizer(stop_words="english", ngram_range=(1, 2), min_df=5),
    representation_model={"KeyBERT": KeyBERTInspired()},
    calculate_probabilities=False, verbose=True)
topics, _ = topic_model.fit_transform(docs, emb)
df["topic"] = topics

info = topic_model.get_topic_info()
rows = []
for _, r in info.iterrows():
    t = r.Topic
    sub = df[df.topic == t]
    games = sub.game.value_counts(normalize=True).head(4)
    rows.append({
        "topic": t, "n": len(sub),
        "share_negative": round((~sub.voted_up).mean(), 3),
        "share_systemic_sandbox": round((sub.group == "systemic_sandbox").mean(), 3),
        "share_knowledge_discovery": round((sub.group == "knowledge_discovery").mean(), 3),
        "share_commercial_control": round((sub.group == "commercial_control").mean(), 3),
        "top_games": "; ".join(f"{g} ({v:.0%})" for g, v in games.items()),
        "terms": ", ".join(w for w, _ in topic_model.get_topic(t)[:10]),
        "keybert_terms": ", ".join(r.KeyBERT[:10]) if isinstance(r.KeyBERT, list) else "",
        "example_1": (r.Representative_Docs[0][:300] if isinstance(r.Representative_Docs, list) else ""),
        "example_2": (r.Representative_Docs[1][:300] if isinstance(r.Representative_Docs, list)
                      and len(r.Representative_Docs) > 1 else ""),
    })
pd.DataFrame(rows).to_csv(f"{out}/bertopic_topics.csv", index=False)
df[["appid", "game", "group", "id", "voted_up", "playtime_at_review_h", "words", "topic"]].to_csv(
    f"{out}/bertopic_assignments.csv.gz", index=False, compression="gzip")
print(f"{len(df)} reviews, {len(info) - 1} topics, {(df.topic == -1).mean():.1%} outliers")
