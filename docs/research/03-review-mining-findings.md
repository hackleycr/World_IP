# What 35,942 Steam Reviews Say About Our Pillars

Status: complete (2026-10-20). Follows the first pass in [02-gameplay-loops-findings.md](02-gameplay-loops-findings.md); plan in [01-gameplay-loops.md](01-gameplay-loops.md).

## Summary

- **In discovery games, discovery is the topic, not the verdict.** Discovery and curiosity language appears in about 30% of substantive reviews of knowledge-progression games, at the same rate in negative and positive reviews (codebook 32% vs 32%; combined method 31% vs 34%). What separates negative reviews is the friction around the discovery:
  - grind and tedium appear in 25% of negative reviews vs 7% of positive ones
  - frustration or being stuck appears in 26% vs 12%
  - opaque rules or a learning curve appear in 14% vs 7%
- **People who dislike discovery games quit early.** Negative reviewers of knowledge-progression games had a median of 5.8 hours of play when they wrote their review. Positive reviewers had 16.8 hours. A first insight has to land well inside the first few hours.
- **The single most-praised cluster is "I wish I could forget this game and play it again."** BERTopic grouped 86 reviews on this, and only 8% of them were negative, against a 63% baseline across all reviews it grouped. Outer Wilds dominates it.
- **The best-received puzzle design is open-ended.** Zachtronics programming/machine puzzles (Opus Magnum, Infinifactory) form a topic that is only 20% negative, against the 63% baseline. Reviewers praise "no 'one' solution, but potentially endless ones".
- **Luck that blocks progress gets heavily punished.**
  - The "RNG in card games" topic is 94% negative.
  - The Noita/Magicka wand-building topic is split between praise for creativity and complaints of "gambling the whole time".
  - Luck/RNG and monetization each appear about 4.4× more often in negative than positive reviews.
- **Destruction itself is not the complaint; inconsistency is.**
  - The destruction-sandbox topic (Teardown, Terraria, RimWorld) is near the baseline at 57% negative.
  - Complaints in it are about physics that break their own rules, e.g. "a building that has 5ft of wall removed on all 4 sides should fall or collapse".
- **Permanence is tolerated when it is signalled, and resented when it is not.** Permanence language is about 2× more frequent in negative reviews. Almost all the negative examples are unannounced lockouts or silent losses.
- **For a simulation-heavy sandbox, stability is not a side issue.**
  - Crashes are the largest cross-game topic: 1,050 reviews, 89% negative.
  - Bugs and performance are the most common theme in negative reviews of sandbox games (19%).

## 1. Data

| Item | Value |
|---|---|
| Games | The 37 Steam titles from [steam-metrics-2026-10.csv](data/steam-metrics-2026-10.csv): 9 systemic/sandbox, 13 knowledge-discovery, 15 commercial control |
| Reviews | 35,942 English reviews, pulled 2026-10-20 from the Steam `appreviews` endpoint, sorted by most recent (`filter=recent`) |
| Sampling | Up to 500 positive and 500 negative reviews per game, so positive and negative reviews are equally represented. Some well-liked games had fewer negative reviews in English: Infinifactory 100, Opus Magnum 136, Heaven's Vault 343, Baba Is You 363. |
| Substantive subset | 16,298 reviews of 20 or more words (10,266 negative, 6,032 positive). Most theme results use this subset, because one-line reviews ("good game") rarely carry a theme. |
| Also recorded | Playtime at the time of the review, Early Access flag, helpful votes |

Because the sample is split evenly between positive and negative reviews, the figures below compare negative with positive reviews within a game group. They are not estimates of how often a theme appears across all of Steam. For that, [theme_weighted_prevalence_by_game.csv](data/review_mining/theme_weighted_prevalence_by_game.csv) reweights each game by its real share of positive reviews.

## 2. Methods, and how far to trust them

Three methods were used, plus manual validation:

1. **Keyword codebook** ([codebook.py](../../research/review_mining/codebook.py)). There are 22 themes, each defined as a set of regular expressions and grouped by pillar. The patterns were tightened over two rounds of checking precision.
2. **BERTopic** ([bertopic_run.py](../../research/review_mining/bertopic_run.py)).
   - Embeddings: `all-MiniLM-L6-v2`. Clustering: UMAP + HDBSCAN, minimum cluster size 60.
   - It found 58 topics across 15,881 substantive reviews, with 33.5% left as outliers.
   - I named each topic by reading its keywords and representative reviews. 22 topics cut across games, 9 are about a genre, and 26 are about a single game. The embeddings group reviews by which game they discuss more than by what they say.
3. **Meaning-based classifier** ([semantic_classify.py](../../research/review_mining/semantic_classify.py)).
   - Each of the 8 pillar themes has 5 seed sentences.
   - A review is tagged with a theme when any of its sentences is close enough in meaning to a seed (cosine ≥ 0.50; the threshold was tuned on the development sample).

**Validation.** The coding was done by Claude, the AI assistant writing this report, not by a human coder. Treat it as a careful single-annotator check, not as inter-rater-reliable ground truth.

- **Precision checks:** 12 matched reviews per theme, in one or two rounds. Results are in [codebook_validation.csv](data/review_mining/codebook_validation.csv).
- **Development sample:** 60 random substantive reviews, coded after seeing the codebook's tags. Used only to tune the classifier's threshold.
- **Blind test sample:** 60 different random reviews, coded before any method's output was viewed. Labels are in [hand_labels.json](data/review_mining/hand_labels.json).

**Results on the blind test sample** (57 theme mentions across the 60 reviews; [method_comparison_test.csv](data/review_mining/method_comparison_test.csv)):

| Method | Precision | Recall | F1 |
|---|---|---|---|
| Keyword codebook | 0.83 | 0.51 | 0.63 |
| Meaning-based classifier alone | 0.62 | 0.32 | 0.42 |
| Union (either method) | 0.67 | 0.61 | 0.64 |

What this means for the results below:

- **When the codebook tags a theme it is usually right, but it misses about half of the real mentions.** It misses misspellings ("repetative"), paraphrase ("5x as long as it should") and plain descriptions of irreversibility ("start over if you die").
  - Raw percentages are therefore lower bounds, roughly half of the true rate.
  - Negative-to-positive comparisons are more reliable, because the misses affect both sides.
- **Sentence embeddings from a small general-purpose model did not beat a tuned keyword list.** Combined with it, they raise recall from 51% to 61% at a cost in precision.
- **The test sample is small.** Per-theme counts are 2–15 mentions, so treat the per-theme figures as indicative only.
- **Robustness check:** I recomputed the pillar-theme comparisons with the union method ([pillar_themes_codebook_vs_union.csv](data/review_mining/pillar_themes_codebook_vs_union.csv)).
  - Every pillar theme's leaning towards negative or positive reviews is the same under both methods.
  - The size changes: grind is 2.7× more common in negative reviews with the codebook, against 1.5× with the union.
  - Content exhaustion is unreliable under both methods (codebook recall 0.20, union precision 0.38), so no conclusion is drawn on it.

## 3. Findings by pillar

All shares below are from substantive reviews (20+ words), using the keyword codebook unless stated otherwise. "Neg/pos" is a theme's share in negative reviews divided by its share in positive reviews. Full tables: [theme_negative_positive_ratio.csv](data/review_mining/theme_negative_positive_ratio.csv), [theme_prevalence_by_group_vote.csv](data/review_mining/theme_prevalence_by_group_vote.csv).

### Pillar 3: discovering and manipulating rules

| Knowledge-discovery games | Negative | Positive | Neg/pos |
|---|---|---|---|
| Discovery / curiosity | 32% | 32% | 1.0 |
| Grind / tedium | 25% | 7% | 3.5 |
| Frustration / stuck | 26% | 12% | 2.1 |
| Learning curve / opacity | 14% | 7% | 2.0 |
| Rewarding / satisfying | 7% | 10% | 0.7 |

- **Discovery is what the game is, so reviewers on both sides talk about it.** The verdict depends on what surrounds the discovery.
  - The games where discovery language is most frequent are Heaven's Vault, TUNIC, Animal Well, Cultist Simulator and Outer Wilds. Their ratings differ widely: Outer Wilds 95.6% positive, Heaven's Vault 83.5%, Cultist Simulator 79.9%.
  - The low-rated ones are the ones whose reviews also carry high grind and opacity scores. Potion Craft, Cultist Simulator and Heaven's Vault lead the grind ranking; Cultist Simulator and Dwarf Fortress lead the opacity ranking.
- **Onboarding is a cross-genre topic of its own.** BERTopic topic 12 ("tutorials, guides and onboarding") has 231 reviews and is 67% negative.
  - Its games are Oxygen Not Included, Cultist Simulator, Dwarf Fortress and Noita. Typical reviews: "The tutorial itself needs a tutorial", and "I don't want to dive into a wiki just to figure out what the hell is happening" (Cultist Simulator).
- **People who dislike discovery games leave early.** Median playtime at the time of the review ([playtime_at_review.csv](data/review_mining/playtime_at_review.csv)):

  | Group | Negative | Positive |
  |---|---|---|
  | Knowledge-discovery | 5.8 h | 16.8 h |
  | Systemic/sandbox | 33.4 h | 94.3 h |
  | Commercial control | 38.2 h | 47.0 h |

- **Open-ended solution spaces are praised.** The Zachtronics topic (152 reviews) is only 20% negative, against the 63% baseline.
  - One review: "A puzzle game with no 'one' solution, but potentially endless ones… This game has more solutions than you can dream of. A total creative win" (Opus Magnum).
  - Complaints in the same topic are about too little challenge ("too unrestricted to be challenging"), not about too much freedom.
- **Replay is the price of a single-solution mystery.** The "wish I could forget it" topic (86 reviews, 8% negative) is the most positive in the study.
  - One reviewer of Outer Wilds wrote: "once you've completed it, you can never experience its magic for the first time again". Positive reviewers love the game and also mourn that it can't be replayed.

### Pillar 1: reward proportional to effort

| All substantive reviews | Negative | Positive | Neg/pos |
|---|---|---|---|
| Monetization | 1.8% | 0.4% | 4.4 |
| Luck / RNG | 5.3% | 1.2% | 4.4 |
| Lost or devalued progress | 1.4% | 0.4% | 3.3 |
| Grind / repetition | 17.6% | 6.5% | 2.7 |
| Rewarding / satisfying | 4.8% | 8.3% | 0.6 |
| Addictive / time sink | 4.4% | 9.0% | 0.5 |

- **Luck that blocks progress is the strongest effort-fairness complaint.** The "RNG in card games" topic (Slay the Spire, Balatro, Cultist Simulator) is 94% negative, the most negative topic in the study.
  - Noita's wand-building topic carries both sides. Some praise creativity ("create your own spell combinations"). Others complain: "it feels like I'm just gambling the whole time. Gambling for wands with any decent spells…".
- **Padding and repetition are what sink games built on combining things.** Potion Craft has the highest grind rate in the dataset (14% of reviews after reweighting).
  - Its reviews describe the loop failing to grow: "you'll keep doing pretty much the same thing for the rest of the game… new ingredients become available… most often it just means it takes longer to make the potion."
- **Lost progress is rare but strongly negative.** Examples:
  - lost saves (Skyrim cloud sync, Heaven's Vault without cloud saves)
  - patches that devalue crafted items (Valheim's item-upgrade change)
  - removed paid content (Destiny 2 "sunsetting")
- **Paid add-ons:** the DLC-pricing topic (407 reviews) is 75% negative. It is led by RimWorld and Diablo IV.

### Pillar 2: actions change the world

- **Destruction is welcome; broken physics is not.** The destruction-sandbox topic (278 reviews, led by Teardown) is 57% negative, slightly below the 63% baseline.
  - Its complaints are about consistency and structure, not destruction itself. One Teardown review: "Came into this expecting a cool physics sandbox but lost interest after the first mission. A building that has 5ft of wall removed on all 4 sides should fall or collapse."
- **Permanence words are 2× more frequent in negative reviews.** The negative examples are nearly all unannounced:
  - "Decisions are randomly permanent and can end exploration of a zone permanently" (Heaven's Vault)
  - items "permanently lost to the void without warning" when a module is deconstructed (Oxygen Not Included)
  - "You can lose a several hours session in a blink of an eye because you did not pay attention to some small detail" (Cultist Simulator)
  - corruption spread that makes the desert "impossible to remove" (Terraria)

  The positive examples describe consequences players chose to accept: "If you like telling stories via surrendering to the consequences of your own actions and mismanagement, I highly recommend…" (RimWorld).
- **World-change language is concentrated in sandbox games.**
  - Destruction / world change: 8% of negative and 5% of positive sandbox reviews.
  - Physics / simulation: 7.5% vs 8.9%.
  - Neither theme leans clearly positive or negative. Players treat the simulation as the setting. Whether they like the game depends on whether the simulation behaves consistently and runs well.

### Engagement and context

- **Building and creating are what sandbox fans praise.**
  - Creativity and building appear in 16% of positive sandbox reviews (codebook) and 13% of negative ones.
  - "Addictive / time sink" appears in 16% of positive sandbox reviews, against 7% of negative ones.
- **Stability:** crashes and stability is the largest cross-game topic (1,050 reviews, 89% negative). Bugs and performance appear in 19% of negative sandbox reviews and developer and update complaints in 21%. A cellular simulation is expensive to run, so performance matters for player sentiment as well as for engineering.
- **Other strongly negative cross-game topics:**

  | Topic | Negative |
  |---|---|
  | Controls | 92% |
  | Early access / unfinished | 88% |
  | Hype backlash | 87% |
  | Cheaters | 84% |

  They affect sentiment but are outside our pillars.

## 4. What this changes for the design

These build on the 16 recommendations in [02-gameplay-loops-findings.md](02-gameplay-loops-findings.md#recommendations-tied-to-the-three-pillars). They add evidence and sharpen four of them.

1. **Get to the first insight within the first hour, not the first session.** Negative reviewers of discovery games quit at a median of 5.8 hours. Tutorials and onboarding are a cross-genre complaint topic.
   - Teach the rules through the first reactions the player sees, such as water cooling lava into stone, rather than through text.
   - The journal should show those observations as open questions straight away. *Strengthens rec. 1.*
2. **Never put repetition between two insights.** In discovery games, grind is what separates negative from positive reviews (3.5× with the codebook, 1.9× with the union method).
   - Recipes must take the repetition out once a player has understood something.
   - Each new tier should change what the player does, not just how long it takes: new tools, primitives or verbs, not longer paths. Potion Craft shows what happens otherwise. *Strengthens recs. 4 and 11.*
3. **Variation must be something the player can learn, never a gamble.** Card-game RNG is the most negative topic in the study, and Noita's wand luck splits its own reviewers.
   - In the randomized-rules mode, every randomized constant has to be discoverable by experiment, using instruments.
   - Never make the player pull a slot-machine lever. *Strengthens recs. 7 and 13.*
4. **Signal permanence before it happens, and make it causal.** Nearly all negative mentions of permanence are unannounced lockouts or silent losses. The positive ones are consequences the player chose.
   - Large irreversible actions should be previewed, with an energy cost and the affected area shown.
   - Silent deletion should never happen.
   - Snapshots or a fossil record of past states remain the safety net. *Strengthens recs. 8–10.*
5. **Physics consistency is a Pillar 3 requirement, not polish.** In Teardown, players' complaints are about structures defying the rules, not about destruction. Any special case in the simulation undermines players' ability to reason about it. *New.*
6. **Make recipes open-ended and score them.** Zachtronics' open solution spaces are among the best-received designs in the dataset, and "too unrestricted to be challenging" is the failure on the other side.
   - Pair freedom with constraints, as Opus Magnum's production puzzles do, and with efficiency histograms. *Confirms rec. 4.*
7. **Treat simulation performance as a design priority.** For a falling-sand world, frame rate and stability determine how players feel about the game. Crashes are the largest negative cluster, and bugs/performance are the top negative theme in sandbox reviews. *New.*

## 5. Limitations

- **Language and recency:** English reviews only, most recent first. They reflect each game's current state (e.g. Helldivers 2's mod policy, Elden Ring's paid cosmetics), not its launch.
- **Platform:** Steam only. Minecraft, the Zelda games and other off-Steam titles are absent.
- **Sampling:** the sample is split evenly between positive and negative reviews. Its shares are comparisons within a group, not estimates for all of Steam.
- **Measurement:**
  - Keyword recall is about 0.5, so absolute rates are understated.
  - Validation was by a single AI coder, on small samples.
  - The meaning-based classifier underperformed.
  - BERTopic topics are partly organized by game rather than by theme.
- **Correlation, not cause:** themes that co-occur with negative reviews may not be what caused the negative verdict.

## 6. Reproducing

```
python3 research/review_mining/pull_reviews.py docs/research/data/steam-metrics-2026-10.csv OUT_DIR 500
cat OUT_DIR/*.jsonl > reviews.jsonl
python3 research/review_mining/analyze.py reviews.jsonl docs/research/data/steam-metrics-2026-10.csv docs/research/data/review_mining
python3 research/review_mining/bertopic_run.py reviews.jsonl BERTOPIC_DIR
python3 research/review_mining/semantic_classify.py score reviews.jsonl SEM_DIR
python3 research/review_mining/semantic_classify.py evaluate SEM_DIR docs/research/data/review_mining/hand_labels.json
```

The review text is not committed, because it is other people's writing and is reproducible from the API. Committed outputs are tables, per-review codes keyed by review ID ([coded_reviews.csv.gz](data/review_mining/coded_reviews.csv.gz), [bertopic_assignments.csv.gz](data/review_mining/bertopic_assignments.csv.gz)) and the hand labels.

## Sources

**Review data (Steam store review endpoint; per-game API URLs are in [steam-metrics-2026-10.csv](data/steam-metrics-2026-10.csv))**
- Steam reviews endpoint, e.g. Noita — https://store.steampowered.com/appreviews/881100?json=1&language=english&filter=recent&review_type=negative&num_per_page=100
- Steam community review pages for the quoted games:
  - Opus Magnum — https://steamcommunity.com/app/558990/reviews/
  - Outer Wilds — https://steamcommunity.com/app/753640/reviews/
  - Noita — https://steamcommunity.com/app/881100/reviews/
  - Potion Craft — https://steamcommunity.com/app/1210320/reviews/
  - Teardown — https://steamcommunity.com/app/1167630/reviews/
  - Heaven's Vault — https://steamcommunity.com/app/774201/reviews/
  - Oxygen Not Included — https://steamcommunity.com/app/457140/reviews/
  - Cultist Simulator — https://steamcommunity.com/app/718670/reviews/
  - RimWorld — https://steamcommunity.com/app/294100/reviews/
  - Terraria — https://steamcommunity.com/app/105600/reviews/

**Methods and tools**
- BERTopic (Grootendorst, 2022) — https://maartengr.github.io/BERTopic/ and https://arxiv.org/abs/2203.05794
- all-MiniLM-L6-v2 sentence embedding model — https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- UMAP — https://umap-learn.readthedocs.io/
- HDBSCAN — https://hdbscan.readthedocs.io/
- scikit-learn TF-IDF and NMF — https://scikit-learn.org/stable/modules/decomposition.html#nmf
- BERTopic outperforming LDA/NMF on Steam reviews (University of Hertfordshire) — https://researchprofiles.herts.ac.uk/en/publications/unravelling-players-insights-a-comparative-analysis-of-topic-mode/

**Prior findings referenced**
- Lin et al. on 10.95M Steam reviews (negative reviews after a median 6.6 h; design complaints dominate), via PC Games Insider — https://www.pcgamesinsider.biz/news/67005/report-bad-design-is-the-no1-complaint-of-steam-user-review-authors
- First-pass findings and the 16 recommendations — [02-gameplay-loops-findings.md](02-gameplay-loops-findings.md)
