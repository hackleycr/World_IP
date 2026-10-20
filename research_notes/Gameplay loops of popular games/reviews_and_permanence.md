# Player Reviews/Behavior Analytics and Player Response to Permanence & World Change

Research date: 2026-10-20. Research tools: web search and fetch. partner.steamgames.com, pcgamesinsider.biz and ojs.aaai.org failed DNS lookup, so some primary documents could not be fetched directly. The notes say where a claim rests on secondary coverage.

---

## A1. What themes drive positive and negative Steam reviews? (Large-scale review mining)

### Takeaway
The best-cited large-scale study is Lin, Bezemer, Zou & Hassan, *Empirical Software Engineering*, 2018. It used about 10.95M reviews across 6,224 games, with data snapshotted in March 2016. In that data, game design and gameplay complaints outnumber bug complaints about 4:1. Negative reviews are written after much less playtime (median 6.6h vs 15.5h for positive reviews). This means players judge "is the core loop good?" early, and design quality, not polish, drives negative sentiment.

### Cited Findings
- **Paper and dataset.** Lin, Bezemer, Zou & Hassan, "An empirical study of game reviews on the Steam platform," *Empirical Software Engineering* (2018), DOI 10.1007/s10664-018-9627-4. The study covers reviews of 6,224 Steam games and asks whether game reviews resemble mobile-app reviews. Its focus is the main concerns users raise and how long players play before reviewing. — [Unpaywall DOI record](https://unpaywall.org/10.1007%2FS10664-018-9627-4); [Queen's SAIL thesis defense slides (Dayi Lin)](https://sail.cs.queensu.ca/data/pdfs/PhD_Thesis_Defense_Dayi.pdf)
- **Sample construction.** In March 2016 Steam had 8,025 games. Removing titles with fewer than 25 reviews left 6,224 games and about 10.95M reviews. Accurate playtime-at-review required a separate real-time crawler, which yielded 28,159 reviews with accurate playing hours. *(Data dated 2016; secondary reporting of the paper.)* — [Kotaku (2018)](https://kotaku.com/deep-study-of-10-million-steam-reviews-is-absolutely-fa-1825908713); [Game Developer, "Going deep in the Steam reviews"](https://www.gamedeveloper.com/production/going-deep-in-the-steam-reviews)
- **Playtime before reviewing.** Players spent a median of 13.5h in a game before reviewing it. Negative reviews came after a median of 6.6h and positive reviews after 15.5h. — [PC Games Insider (2018), as summarized in search results](https://www.pcgamesinsider.biz/news/67005/report-bad-design-is-the-no1-complaint-of-steam-user-review-authors); [PCGamesN](https://www.pcgamesn.com/steam-bad-reviews-study). *Note: Kotaku and other coverage call 13.5h the "average".*
- **Design vs bugs.** Across all reviews, about 34% mention game design problems and about 8% mention bugs. Among negative reviews, about 57% mention design and about 17% mention bugs. "Bad game design" is defined broadly as gameplay problems. — [PC Games Insider](https://www.pcgamesinsider.biz/news/67005/report-bad-design-is-the-no1-complaint-of-steam-user-review-authors); [CogConnected (May 2018)](https://cogconnected.com/2018/05/study-gamers-shown-care-poor-design-bugs/)
- **Usefulness.** Only about 42% of reviews contain "valuable" feedback (specific pros, cons or bug reports). 71% of positive reviews were judged not helpful to developers, versus 55% of negative reviews. — [Kotaku](https://kotaku.com/deep-study-of-10-million-steam-reviews-is-absolutely-fa-1825908713); [PC Games Insider](https://www.pcgamesinsider.biz/news/67005/report-bad-design-is-the-no1-complaint-of-steam-user-review-authors)
- **Length and type.** The average review is about 30 words. Early Access and indie games get longer reviews, and free-to-play games get shorter ones. Early Access reviews tended to be more positive than reviews of finished titles. — [Kotaku](https://kotaku.com/deep-study-of-10-million-steam-reviews-is-absolutely-fa-1825908713); [PC Games Insider](https://www.pcgamesinsider.biz/news/67005/report-bad-design-is-the-no1-complaint-of-steam-user-review-authors)
- **Helpfulness vs playtime (separate study, 26.8M Steam reviews).** The most-helpful positive reviews come from users with either the most or the least experience. The most-helpful negative reviews come from users with moderate experience. — [Kellogg Insight](https://insight.kellogg.northwestern.edu/article/helpfulness-of-online-reviews)
- **Conflicting evidence.** A 2024 study of VR games found no correlation between review polarity and playtime before review. This conflicts with Lin et al., though it covers a different population. *(Reported in search summary; primary not fetched.)* — [search context via PCGamesN coverage thread](https://www.pcgamesn.com/steam-bad-reviews-study)

### Inferences
- Negative reviewers decide after about 6–7 hours. For a discovery-driven sandbox, the first few hours have to show that insight pays off. If the payoff from deep systems arrives later than that, the game will be reviewed on its early hours.
- "Design" complaints dominate. Systemic games are most exposed to design-legibility complaints (opaque rules, feeling cheated), more than to bugs.
- Early Access reviews skew longer and more positive. An Early Access phase is a good channel for qualitative feedback on rule discoverability.

### Gaps
- I did not retrieve the full Lin et al. paper. Its taxonomy of review topic categories, and how strongly each category predicts a recommendation, could not be checked beyond the design and bug percentages.
- The data is from 2016. I found no peer-reviewed replication on 2023–2026 Steam data.

---

## A2. Playtime distributions, ownership without play, completion and churn

### Takeaway
About a quarter to a third of purchased Steam games are never launched. Typical story-game completion rates are 20–40%, with the median game finished by about a third of players. Players vary greatly in how much they persist, so only a small share of a game's owners ever see its late content.

### Cited Findings
- **Ars Technica "Steam Gauge" (April 2014).** It sampled about 250,000 random public Steam profiles over 3 days. It first reported that 36.9% of purchased games had never been loaded and a further 17% were played for less than an hour. — [Shacknews (2014)](https://www.shacknews.com/article/84088/report-37-of-steam-games-are-never-played)
- **Revision.** Ars later corrected for the fact that Steam began recording "hours played" only in March 2009. The never-played figure fell to about 26.5%. — [Game Informer (2014-04-16)](https://gameinformer.com/b/news/archive/2014/04/16/over-one-third-of-purchased-steam-games-have-never-been-played)
- **Later independent estimate (GameDiscoverCo, using GamingAnalytics.info data).** The average Steam library is 32.7% unplayed. The median player has 51.5% of their library unplayed. — [GameDiscoverCo newsletter](https://newsletter.gamediscover.co/p/how-many-pc-games-get-bought-but-not-played)
- **Completion via achievements.** Steam's main-story achievement was earned by 26.6% of Elden Ring players and 23.7% of Witcher 3 players. Another analysis found the median game was finished by about 36% of players. — [Den of Geek](https://www.denofgeek.com/?p=824046)
- **Academic achievement datasets:**
  - arXiv 2404.15295 analyzes Steam achievement unlock fractions for games released 2004 to January 2021, treating them as a measure of player persistence. — [arXiv 2404.15295](https://arxiv.org/html/2404.15295v1)
  - Bailey & Miyata, "Improving video game project scope decisions with data: An analysis of achievements and game completion rates." Its dataset covers games through 2016. — [Mendeley Data](https://data.mendeley.com/datasets/jc37n76wyt)
- **Cross-game behavior at scale.** Sifa, Drachen & Bauckhage, "Large-Scale Cross-Game Player Behavior Analysis on Steam," AIIDE 2015. The full text could not be fetched (DNS failure). — [AAAI OJS](https://ojs.aaai.org/index.php/AIIDE/article/view/12804)
- **Caution.** A voxbooster.com page claiming a 26.4% campaign completion rate for 2026 cites sources without links or methods. Treat it as unreliable. — [voxbooster](https://voxbooster.com/blog/game-difficulty-completion-statistics-2026/)

### Inferences
- Design for the roughly 25–35% of owners who never start the game (wishlist and store conversion) separately from players who drop off in early sessions.
- Completion achievements give a usable persistence curve. A sandbox should define milestone "discovery" achievements so it can measure how deep players get into discovering rules.

### Gaps
- I found no reliable published session-length or day-1/day-7/day-30 churn benchmarks for premium PC sandbox games with sources.
- I could not retrieve the Sifa et al. (2015) quantitative findings, such as how concentrated playtime is.

---

## A3. Methods to replicate: Steam review API, topic tagging (LDA/BERTopic/LLM), SteamSpy/SteamDB

### Takeaway
Reviews can be scraped at full scale with cursor pagination from `store.steampowered.com/appreviews/<appid>?json=1`, at up to 100 reviews per page. For topic tagging, BERTopic beats LDA and NMF on coherence for Steam reviews. LLM labeling of BERTopic clusters is an emerging practice, but peer-reviewed validation is still thin.

### Cited Findings
- **API pagination and page size (secondary sources; Valve's partner doc could not be fetched).**
  - The partner doc template is `store/getreviews` with `json=1&num_per_page=100`. Pass `cursor=*` for the first page, then reuse the returned cursor. — [Apify scraper doc](https://apify.com/venturesome_laugh/steam-reviews-scraper.md)
  - Cursor values must be URL-encoded. — [PyPI steam-reviews](https://pypi.org/project/steam-reviews/0.1.0)
  - `num_per_page` has a maximum of 100. Larger values are silently clamped. — [Glama MCP tool doc](https://glama.ai/mcp/servers/fenxer/steam-review-mcp/tools/get_steam_review); [Apify](https://apify.com/venturesome_laugh/steam-reviews-scraper.md)
  - Sources conflict on the default page size: 20 vs 50. — [PyPI](https://pypi.org/project/steam-reviews/0.1.0) vs [Glama](https://glama.ai/mcp/servers/fenxer/steam-review-mcp/tools/get_steam_review)
  - Aggregate totals (`query_summary`) are populated only on the first page (`cursor=*`). — [Crawlora tool doc](https://policylayer.com/tools/crawlora-mcp/steam-reviews)
  - `store.steampowered.com/robots.txt` does not restrict `/appreviews/`. — [Apify scraper doc](https://apify.com/venturesome_laugh/steam-reviews-scraper.md)
  - Official reference (unfetched): [partner.steamgames.com/doc/store/getreviews](https://partner.steamgames.com/doc/store/getreviews)
- **Topic-model comparison.** "Unravelling players' insights: a comparative analysis of topic modelling" (IEEE Transactions on Games, 2024; Univ. of Hertfordshire) compared LDA, NMF and BERTopic on No Man's Sky Steam reviews. BERTopic had the highest coherence (0.279). The authors also interviewed 7 developers about whether the output was useful. — [Herts research profile](https://researchprofiles.herts.ac.uk/en/publications/unravelling-players-insights-a-comparative-analysis-of-topic-mode/); [accepted version PDF](https://uhra.herts.ac.uk/id/eprint/11234/1/accepted_version.pdf)
- **LDA applied at scale.** About 130,000 Steam reviews of the Dark Souls series yielded 14 topics for DS3 and 15 for DS1. — [CMS conference paper](https://openaccess-api.cms-conferences.org/articles/download/978-1-7923-8989-4_22)
- **BERTopic plus an LLM for labels.** A 2025 undergraduate thesis used BERTopic plus Qwen2.5 to label topics, evaluated with C_V, U_Mass and C_NPMI, and with cosine similarity for the LLM labels. — [Universitas Sriwijaya repository](https://repository.unsri.ac.id/175059/24/RAMA_55201_09021282126114_0018048003_01_front_ref.pdf)
- **Datasets.** A public Steam review dataset is on Mendeley. — [Mendeley 89yxn7hmpt](https://data.mendeley.com/datasets/89yxn7hmpt/1)

### Inferences
- **Replication pipeline:**
  1. Pull all reviews per app using cursor pagination, `filter=recent` or `filter=updated`, `language=all`, and `num_per_page=100`.
  2. Keep the playtime-at-review and recommendation fields.
  3. Cluster with BERTopic.
  4. Have an LLM label the clusters, then code a sample of reviews with an LLM using a fixed codebook. The codebook should include design/gameplay, bugs, performance, price, content amount, difficulty/fairness, permanence/"lost progress", and UI/legibility.
  5. Validate against roughly 300 human-coded reviews.
  6. Regress the recommendation on topic presence plus playtime.

### Gaps
- Valve's official parameter list and rate limits were not verified because the partner site was unreachable from this environment.
- SteamSpy and SteamDB access terms and accuracy were not researched within the tool budget. SteamSpy's owner estimates have been less precise since Valve's 2018 privacy change. That point comes from background knowledge and is unverified here.
- I found no peer-reviewed 2023–2026 study validating LLM coding of Steam reviews against human coders.

---

## B1. Player response to permanent consequences (permadeath, hardcore, wipes, persistent destruction)

### Takeaway
Most players avoid opt-in hardcore modes: under 10% of Diablo III characters were Hardcore. Among players who do choose permanence, losses are experienced positively when they feel *meaningful*. A death or loss is judged negative mainly when it seems arbitrary or meaningless. Large-scale permanent destruction, as in EVE, becomes memorable history rather than a reason to churn.

### Cited Findings
- **Copcic et al. (2013).** A survey of 1,704 respondents on permadeath found that a death is judged negative mainly when the player sees it as "meaningless". — [Carter & Allison, "Fear, loss and meaningful play: Permadeath in DayZ," JGVW 9(2), citing Copcic](https://www.doi.org/10.1386/jgvw.9.2.143_1)
- **Carter & Allison (DayZ, 2017).** Permadeath loss is experienced positively only if it is meaningful, in Salen & Zimmerman's sense of meaningful play. The authors link its appeal to excitation transfer. — [Intellect JGVW 9(2)](https://www.doi.org/10.1386/jgvw.9.2.143_1)
- **Experiment with 65 participants (Don't Starve Together; NCCU thesis).** Permadeath significantly increased frustration at death. The meaning players attributed to the death mediated the link between frustration and willingness to keep playing, so frustration turned into motivation. — [NCCU repository](https://nccur.lib.nccu.edu.tw/handle/140.119/159388)
- **WVU dissertation (N=394).** Players reported greater appreciation of permadeath through grief over lost characters. The effect was stronger for players attached to their characters. — [WVU Research Repository](https://researchrepository.wvu.edu/etd/7614)
- **MIT pilot (Bowie-Wilson, "Roguelife").** A small sample comparing a roguelike with and without permadeath suggested permadeath may improve perceptions of play. The author says it is not generalizable. — [MIT CMS](https://cms.mit.edu/roguelife-digital-death-in-videogames-and-its-design-consequences)
- **Diablo III Hardcore uptake (Blizzard one-year figures, 2013).** Only about 9% of the 67.1M characters created were Hardcore. Europe had the highest Hardcore share, then the Americas, then Asia. — [Next INpact](https://next.ink/30091/79890-diablo-iii-deux-infographies-retracent-premiere-annee-jeu/); [Millenium](https://www.millenium.org/news/118995.html); [PC Gamer](https://www.pcgamer.com/au/diablo-3-one-year-anniversary-infographic-unleashes-hellishly-huge-numbers)
- **Diablo III Hardcore deaths.** The largest share of Hardcore deaths (35%) happened in Act I Normal, i.e. early. — [GosuGamers](https://www.gosugamers.net/diablo/features/36947-game-design-updates-a-short-analysis)
- **Diablo IV Hardcore.** Blizzard's Lilith statue reward for reaching level 100 in Hardcore was capped at the first 1,000 players. One player died at 95% of the way to level 100 after about 150 hours. I found no official share of Hardcore players. — [Mein-MMO](https://mein-mmo.de/diablo-4-spieler-stirbt-in-hc-kurz-vor-level-100/)
- **EVE Online, Bloodbath of B-R5RB (January 2014).**
  - About 21 hours of fighting destroyed about 11 trillion ISK of ships, including 75 Titans.
  - Real-world value is estimated at about US$300k–330k via PLEX prices. Other estimates range from $200k to $500k.
  - The trigger was a missed sovereignty maintenance payment.
  - — [Wikipedia](https://en.wikipedia.org/wiki/Battle_of_B-R5RB); [UCSB Bottom Line](https://thebottomline.as.ucsb.edu/?p=20461); [BreakingNews.ie](https://www.breakingnews.ie/discover/heres-what-200000-of-real-money-being-destroyed-in-a-game-looks-like-621193.html)
- **EVE, M2-XFE.** The Massacre at M2-XFE later destroyed about 23T ISK, roughly $347k. — [Nowiknow](https://nowiknow.com/the-real-cost-of-fake-war/)
- **Rust wipes.**
  - Wipes are standard practice: Facepunch forces a monthly wipe. — [Host Havoc KB](https://hosthavoc.com/billing/knowledgebase/62/How-to-wipe-your-Rust-serviceandsharp039s-player-data-and-world-or-both.html)
  - Hosts recommend wiping about every 30 days "to keep the community active". — [Fragnet docs](https://docs.fragnet.net/games/rust/rust-wipe)
  - RUSTalyzer measures each server's "Wipe Players" (average peak concurrent players on wipe day over the last 6 wipes) and "Half-Life" (days until population falls below 50% of peak). Its data shows population surging at each wipe and decaying afterwards. — [RUSTalyzer wipe quality metrics](https://www.rustalyzer.com/blog/server-wipe-quality-metrics)
  - A hosting operator's opinion piece calls wipe cadence "the strongest retention lever". — [Supercraft](https://supercraft.host/article/rust-wipe-cadence-strategy-weekly-vs-biweekly-without-killing-population/)

### Inferences
- Opt-in permanence appeals to a minority (around 10% in Diablo III), but those players are highly engaged. Making permanence the *default* needs losses that read as meaningful and caused by the player. "Meaningless" losses from opaque rules are what players resent.
- Rust's wipe cycle shows that periodic resets can *drive* retention: a fresh start brings players back. A world that can be ruined is acceptable if the game makes a new world, or a new chapter, attractive.
- EVE shows how player-caused permanent destruction from a legible cause (a missed payment) becomes celebrated lore and press coverage.

### Gaps
- I found no official Minecraft Hardcore usage statistics.
- I found no Facepunch-published retention figures for wipes. The RUSTalyzer half-life numbers are per-server and were not aggregated here.
- Dwarf Fortress ("Losing is fun"), Frostpunk, Factorio pollution, From Dust, Black & White and Populous were not researched within the tool budget. I have no sourced quantitative data on player responses to them.

---

## B2. Does persistent world change and ownership increase attachment or retention?

### Takeaway
Lab evidence (the IKEA effect) shows that effort raises how much people value what they made, but **only when the creation is completed and intact**. The effect disappears when the creation is destroyed. I found no controlled game-specific study.

### Cited Findings
- **Norton, Mochon & Ariely (2012), "The IKEA Effect: When Labor Leads to Love."** Four studies used IKEA boxes, origami and Lego. Self-made products were valued more highly, and participants rated their amateur creations about as highly as experts' work. The effect disappeared when participants built and then destroyed their creations, or failed to complete them. — [SSRN](https://papers.ssrn.com/abstract=1777100); [HBS Working Knowledge](https://hbswk.hbs.edu/item/6671.html); [Harvard DASH](https://dash.harvard.edu/handle/1/12136084)
- **Extension to user-generated content.** Mochon argues the effect explains why user-generated-content platforms work. This is commentary, not a controlled study. — [Tulane Freeman News](https://freemannews.tulane.edu/print/pdf/node/2621)
- **Unverified claim.** A cited 2014 study (Lee et al.) reportedly found that effort raises the value of digital content. I could not locate the original. — [Learning Loop](https://learningloop.io/plays/psychology/ikea-effect)

### Inferences
- In a sandbox where players can damage the world, the IKEA finding cuts both ways. Effort spent shaping the world raises attachment, but seeing their own creation destroyed may erase that value.
- **Design implication:** give players ways to *finish* and preserve work, such as snapshots, journals, museums or "fossil records" of past states, even when the live world can be ruined.

### Gaps
- I found no study measuring whether player housing, base building or world persistence raises retention.

---

## B3. Failure modes: ruined worlds, griefing, save-scumming, and mitigations

### Takeaway
The clearest shipped mitigation for irreversible world spread is Terraria's. Corruption, Crimson and Hallow spread in Hardmode, and Journey Mode (1.4) added a toggle to *stop* spread, though not to reverse it. Griefing in shared persistent worlds is more widespread than expected. Save-scumming is under-researched; designers counter it with built-in rewind or by making failure states interesting.

### Cited Findings
- **Terraria spread.** Corruption, Crimson and Hallow are the only biomes that spread, converting nearby tiles. Spread starts in Hardmode. Containment requires digging tunnels 3–6 tiles wide around protected areas. Desktop 1.2.0.3 slowed spread after Plantera is defeated. — [Terraria Wiki: Maintaining world purity](https://terraria.wiki.gg/Guide:Maintaining_world_purity); [Terraria Wiki: Spread](https://terraria.wiki.gg/wiki/Spread)
- **Terraria Journey Mode (1.4, 2020).** A Power Menu toggle halts the spread of Corruption, Crimson and Hallow. It does not reverse spread or prevent the diagonal biome stripes created when Hardmode starts. — [Terraria Wiki: Journey Mode](https://terraria.wiki.gg/wiki/Power_Menu); [BisectHosting](https://www.bisecthosting.com/it-it/blog/terraria-journey-mode)
- **Minecraft griefing.** Matthews (AUT thesis) found that a larger share of players grief than expected and that griefing affected many players, but found no organized harassment community. — [AUT repository](https://openrepository.aut.ac.nz/bitstream/handle/10292/12787/MatthewsB.pdf)
- **"Good" Grief (2016).** An analysis of Minecraft griefing guides found they promote a utilitarian, schadenfreude ethic that conflicts with players' cooperative norms. — [Scinapse](https://www.scinapse.io/papers/2432104859)
- **Griefer vs victim perceptions (MMO survey).** Self-identified griefers were more likely to see the same actions as part of the game rather than as griefing. Authors are unverified. — [Springer Professional](https://www.springerprofessional.de/doi/10.1145/2513002.2513007)
- **Save-scumming research.** Farmer & Kelly (BPS) called it under-researched in media psychology. A 2025 DiGRA extended abstract proposes a qualitative study using self-determination theory (UK and US); no results yet. — [BPS](https://bps.org.uk/news/save-scumming-role-playing-games-call-further-psychological-exploration); [DiGRA library](https://dl.digra.org/index.php/dl/article/view/2509)
- **Designer mitigations.**
  - Shadow Gambit (Mimimi) made quick-save a central mechanic, and uses variety in encounters to pull players away from repetitive reloading. — [Game Developer](https://www.gamedeveloper.com/design/how-shadow-gambit-the-cursed-crew-was-able-to-make-save-scumming-a-central-mechanic)
  - A PC Gamer feature argues for designing out the "reloading trap" with unerasable but interesting failure states (e.g. a Crusader Kings III succession crisis), or for building rewind into the game, as racing games do. — [PC Gamer (Feb 2024, via Readly)](https://gb.readly.com/magazines/pc-gamer-uk/2024-02-29/65d9e1a9f37eb51b935e9654)

### Inferences
- **Mitigation set for a ruinable world:**
  1. Make spread visible early and slow, Terraria-style, with player tools to contain it.
  2. Offer a "pause spread" accessibility toggle, as Journey Mode does.
  3. Make failure states produce new content rather than dead ends: a ruined area should create new ecology or rules to discover, not just loss.
  4. Provide a diegetic rewind or snapshot instead of fighting save-scumming.
  5. In multiplayer, use claims or permissions to limit griefing.
- Because players judge losses by meaningfulness (B1), a ruined world should be clearly *caused by the player and understandable*. Insight into why it collapsed is itself the reward, which fits an "insight over grind" design.

### Gaps
- I found no quantitative data on how many players abandon a save or world after irreversible damage in any game.
- I found no measured save-scum rates.
- Spore, From Dust, Black & White, Populous, Frostpunk and Factorio reception data were not gathered.
