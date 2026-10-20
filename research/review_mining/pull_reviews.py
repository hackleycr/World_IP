"""Pull a stratified sample of English Steam reviews (N positive + N negative, most recent first)
for every app in docs/research/data/steam-metrics-2026-10.csv.

Writes one JSONL file per app into OUT_DIR, one review per line. Apps whose file already exists are
skipped, so an interrupted pull can be resumed.

Usage: python3 pull_reviews.py steam-metrics.csv OUT_DIR PER_CLASS
"""
import csv, json, os, sys, time, urllib.parse, urllib.request

METRICS, OUT, PER_CLASS = sys.argv[1], sys.argv[2], int(sys.argv[3])
UA = {"User-Agent": "Mozilla/5.0 (World_IP research)"}


def fetch(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.loads(r.read())
        except Exception as e:
            err = e
            time.sleep(2 ** (i + 1))
    raise RuntimeError(f"{url}: {err}")


def pull(app, vote, out):
    cursor, got, seen = "*", 0, set()
    while got < PER_CLASS:
        url = ("https://store.steampowered.com/appreviews/{}?json=1&language=english&filter=recent"
               "&purchase_type=all&review_type={}&num_per_page=100&cursor={}").format(
                   app["appid"], vote, urllib.parse.quote(cursor))
        j = fetch(url)
        new = [r for r in j.get("reviews", []) if r["recommendationid"] not in seen]
        if not new:
            break
        for r in new[: PER_CLASS - got]:
            seen.add(r["recommendationid"])
            out.write(json.dumps({
                "appid": int(app["appid"]), "game": app["name"], "group": app["group"],
                "id": r["recommendationid"], "voted_up": r["voted_up"],
                "playtime_at_review_h": round(r["author"].get("playtime_at_review", 0) / 60, 1),
                "playtime_forever_h": round(r["author"].get("playtime_forever", 0) / 60, 1),
                "created": r["timestamp_created"], "votes_up": r["votes_up"],
                "early_access": r.get("written_during_early_access", False),
                "text": r["review"]}) + "\n")
            got += 1
        cursor = j.get("cursor", "")
        time.sleep(0.7)
    return got


os.makedirs(OUT, exist_ok=True)
for app in csv.DictReader(open(METRICS)):
    path = os.path.join(OUT, f"{app['appid']}.jsonl")
    if os.path.exists(path):
        continue
    with open(path + ".part", "w") as out:
        counts = {vote: pull(app, vote, out) for vote in ("positive", "negative")}
    os.rename(path + ".part", path)
    print(app["name"], counts, flush=True)
