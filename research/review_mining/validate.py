"""Draw hand-coding samples to measure codebook accuracy.

precision sample: for each key theme, N reviews the codebook tagged with it (does the review really discuss it?)
recall sample:    M random substantive reviews; a human codes all key themes, then compare to the codebook.

Usage: python3 validate.py reviews.jsonl out_dir [N=12] [M=60]
"""
import json, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codebook import code  # noqa: E402

KEY = ["grind_repetition", "progress_loss_devaluation", "discovery_curiosity", "learning_curve_opacity",
       "creativity_building", "emergence_simulation", "permanence_consequence", "content_runs_out"]

src, out = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 12
m = int(sys.argv[4]) if len(sys.argv) > 4 else 60
os.makedirs(out, exist_ok=True)
rng = random.Random(42)
reviews = [json.loads(l) for l in open(src)]
reviews = [r for r in reviews if 20 <= len(r["text"].split()) <= 250]
for r in reviews:
    r["codes"] = sorted(code(r["text"]) & set(KEY))

with open(f"{out}/precision_sample.jsonl", "w") as f:
    for t in KEY:
        pool = [r for r in reviews if t in r["codes"]]
        for r in rng.sample(pool, min(n, len(pool))):
            f.write(json.dumps({"theme": t, "id": r["id"], "game": r["game"], "text": r["text"]}) + "\n")

with open(f"{out}/recall_sample.jsonl", "w") as f:
    for r in rng.sample(reviews, m):
        f.write(json.dumps({"id": r["id"], "game": r["game"], "codebook": r["codes"], "text": r["text"]}) + "\n")
