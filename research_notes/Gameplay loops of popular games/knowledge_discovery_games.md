# Gameplay Loops of Knowledge-Progression and Rule-Discovery Games

> Research date: 2026-10-20. **Method caveat:** store.steampowered.com, steamcommunity.com, api.steampowered.com, and en.wikipedia.org did not resolve from this research environment (DNS failure / proxy 403), and WebFetch was unusable. All findings come from web-search result content, with the source URL each one came from. SteamDB, Steam achievement global stats, HowLongToBeat, and Metacritic could not be read directly. Wherever a number is missing, this is listed under Gaps. Numbers are dated by their source's date where known. Otherwise they are marked "as indexed Oct 2026".

## Q1. Loop breakdowns and quantitative signals per game

### Takeaway
In these games, the progress that matters is stored in the player's head, not in their inventory. The loop is: probe → observe rule → form hypothesis → test → new mental capability → probe further. Sales range widely. Fez reached about 1M by 2013. Outer Wilds has an estimated 1.8–3.7M on Steam. Cultist Simulator sold about 40k at launch. Steam review scores are very high where available (Outer Wilds ~94–96%). Hard per-game data was not retrievable for most titles in this session.

### Cited Findings

**Outer Wilds (Mobius Digital, 2019)**
- Creative director Alex Beachum (2023 interview): the game is "all knowledge-gated. So if you know everything, you can just boop-da-boop-da-boop." Each "Curiosity" has about three clues/rules to learn, and the team avoids putting two rules for the same Curiosity on one planet — [Medium interview with Alex Beachum](https://medium.com/@cordialkobold/interview-with-alex-beachum-creative-director-of-outer-wilds-a01bb9631e20)
- Beachum originally envisioned the game as a roguelike with randomized elements. It moved to a fixed solar system with a time loop to better serve its story and design. The ship log splits the story into four "curiosity webs" so players can uncover the mystery in any order — [The Fourth Curtain podcast (Spotify)](https://open.spotify.com/episode/0iuocjlbq4hWDV7B0y3smJ); [Apple Podcasts listing](https://podcasts.apple.com/us/podcast/outer-wilds-alex-beachums-cool-weird-emotional-prototypes/id1671350556?i=1000702968300)
- GDC 2020 talk "Curiosity-Driven Exploration: The Design of 'Outer Wilds'" by co-creative leads Alex Beachum and Loan Verneau. It covers the meta design, from 2D prototypes to the final mystery structure. (The assignment's title "Designing for Curiosity" appears to refer to this talk.) — [GDC announcement](https://gdconf.com/article/attend-gdc-and-learn-how-outer-wilds-nailed-curiosity-driven-game-design/); [Game Developer](https://www.gamedeveloper.com/design/attend-gdc-and-learn-how-i-outer-wilds-i-nailed-curiosity-driven-game-design)
- Ship Log "Rumor Mode": entries are cards split into "rumor facts" and "explore facts". Curiosities are the big story threads, such as the Ash Twin Project — [New Horizons modding docs, Ship Log](https://nh.outerwildsmods.com/guides/ship-log/). An academic analysis says Rumor Mode guides players to new points of interest "by showing the relationship of information" — [Cuthbertson, "The Ship Log in Outer Wilds" (PDF)](https://paigecuthbertson.com/pdfs/The_Ship_Log_in_Outer_Wilds.pdf?target=%22_blank%22)
- The game shows "There's more to explore here" when an important entry is still missing. Non-essential entries do not trigger it — [Steam guide: Ship Log Completion](https://steamcommunity.com/sharedfiles/filedetails/?id=3500382207)
- Sales estimates (third-party, as indexed Oct 2026; Valve does not publish sales):
  - Raijin: ~1.8M Steam copies and ~$27.5M gross — [Raijin](https://raijin.gg/app/753640/Outer_Wilds)
  - Sensor Tower: 3.2M paid units — [Sensor Tower](https://app.sensortower.com/vgi/game/outer-wilds)
  - Steam Page Analyzer: 3,744,804 copies (review-count method) — [Steam Page Analyzer](https://www.steampageanalyzer.com/tools/revenue-calculator/753640)
  - Levvvel: "over 2 million" across all platforms — [Levvvel](https://levvvel.com/outer-wilds-statistics/)
- Steam reviews (as indexed Oct 2026; the sources disagree): 96% of 106,194 per Raijin — [Raijin](https://raijin.gg/app/753640/Outer_Wilds); 94.21% SteamDB rating on ~109k reviews — [SteamDB](https://steamdb.info/app/753640/); 95% of 90,173 per IsThereAnyDeal — [ITAD](https://isthereanydeal.com/game/outer-wilds/info/)
- Achievements: 31 total. The most common are above 30% and several are in single digits or low teens. Individual names and percentages could not be read — [Steam Global Achievement Stats](https://steamcommunity.com/stats/753640/achievements)

**Baba Is You (Hempuli / Arvi Teikari, 2019)**
- Origin: the jam theme "Not There" led to the logical NOT operator and the idea of a Sokoban-like game built around it — [GamesBeat](https://gamesbeat.com/the-indiebeat-baba-is-you-is-a-charming-puzzle-game-where-words-matter/)
- Teikari, as a solo developer, became "blind" to his levels' difficulty. Puzzles he thought too easy turned out to be very hard. The basic concept is simple, but players must absorb a lot of underlying logic — [MCV/DEVELOP "When We Made… Baba Is You"](https://mcvuk.com/development-news/when-we-made-baba-is-you/)
- Teikari discusses the balance between freedom and constraining player expression, and the pacing and sequencing of puzzles — [Nice Games Club ep. 373](https://nicegames.club/episode/373). A GDC-derived video breakdown is at [Game Developer "Understanding the rules of Baba Is You"](https://www.gamedeveloper.com/design/video-understanding-the-rules-of-i-baba-is-you-i-)

**Return of the Obra Dinn (Lucas Pope, Oct 18 2018 PC/Mac; Oct 18 2019 consoles)**
- The player must "determine the fates of all sixty souls aboard". The game won the Seumas McNally Grand Prize, among other awards — [Wikipedia (via search)](https://en.wikipedia.org/wiki/Return_of_the_Obra_Dinn)
- Pope on marketing: "if I can make the right kind of game then it's not something that needs to sell in the first 3 months only" — [Game Developer](https://www.gamedeveloper.com/business/why-lucas-pope-didn-t-market-i-return-of-the-obra-dinn-i-)
- Third-party gross revenue estimate: ~$16.46M (unverified) — [Steam Revenue Calculator](https://steam-revenue-calculator.com/app/653530/return-of-the-obra-dinn)
- Pope's making-of talk — [Game Developer](https://www.gamedeveloper.com/design/watch-lucas-pope-discuss-the-making-of-i-return-of-the-obra-dinn-i-)

**The Witness (Thekla / Jonathan Blow, Jan 2016)**
- Sold "substantially" more than 100,000 copies on PS4 and PC in its first week. It grossed over $5M in the first week, before platform fees and taxes, and had not yet broken even. The game was priced at $40 — [Game Developer](https://www.gamedeveloper.com/business/-i-the-witness-i-has-grossed-over-5-million-selling-100k-in-a-week); [GameSpot](https://www.gamespot.com/articles/the-witness-sells-100000-copies-xbox-one-version-b/1100-6434441/); [PCGamesN](https://www.pcgamesn.com/the-witness/the-witness-due-to-sell-more-in-a-week-than-braid-sold-in-its-first-year)
- Blow: "The game is designed to create many opportunities for epiphany moments, both small and large"; "The Witness is about modelling the feeling of epiphany with great care" — [Game Developer "Modeling epiphany"](https://www.gamedeveloper.com/design/-i-the-witness-i-modeling-epiphany); [Game Developer Q&A](https://www.gamedeveloper.com/business/q-a-jonathan-blow-on-i-the-witness-i-and-the-state-of-indie-games)

**Fez (Polytron, 2012)**
- Passed 1M copies across Xbox 360, PC, Mac, and Linux (announced Dec 2013) — [Game Developer](https://www.gamedeveloper.com/business/-i-fez-i-has-sold-more-than-1-million-copies); [Engadget, 2013-12-09](https://www.engadget.com/2013-12-09-fez-sales-surpass-1-million.html); [Shacknews](https://www.shacknews.com/article/82285/fez-sells-a-million-copies-across-all-platforms)

**Tunic (Isometricorp / Finji, 2022)**
- Steam sales estimates (third-party, as indexed Oct 2026):
  - Gamalytic: ~748.9K (range 527.7K–970.1K) — [Gamalytic](https://gamalytic.com/game/553420)
  - GameRevenueData: 809.8K–891.4K — [GameRevenueData](https://gamerevenuedata.com/games/tunic/)
  - Indielist: 641K–1.5M (median ~1.1M) — [Indielist](https://indielist.games/games/tunic)

**Animal Well (Billy Basso / Bigmode, May 2024)**
- Basso estimated ~650,000 copies across Windows, PS5, and Switch (August 2024) — [Wikipedia (via search)](https://en.wikipedia.org/wiki/Animal_Well)
- Third-party estimates: Sensor Tower 801k Steam units — [Sensor Tower](https://app.sensortower.com/vgi/game/animal-well); GameRevenueData 1.1–1.2M on Steam — [GameRevenueData](https://gamerevenuedata.com/games/animal-well/)
- The community's response to the pre-release ARG puzzles gave Basso confidence to build complex puzzles. Basso: "People really appreciated the secrets in the game." He expected a hardcore audience, while most players would simply enjoy the game — [Game Developer](https://www.gamedeveloper.com/design/why-animal-well-s-home-brewed-engine-was-key-to-its-success)

**Cultist Simulator (Weather Factory / Alexis Kennedy, May 2018)**
- Sold over 40k copies across storefronts two weeks after launch. The team's year-one projections were 10k (pessimistic) to 30k (optimistic) — [Kennedy, "After the Dawn"](https://medium.com/@alexiskennedy/after-the-dawn-what-happened-when-we-launched-cultist-simulator-4ea9a60b503). Sales were about 5× expectations — [Game Developer retrospective](https://www.gamedeveloper.com/business/cultist-simulator-the-retrospective). Gross sales were over $1.76M by Feb 2019 — [Wikipedia (via search)](https://en.wikipedia.org/wiki/Cultist_Simulator)

**Potion Craft: Alchemist Simulator (niceplay games / tinyBuild)**
- Sold over 100,000 units on Steam in 3 days (early access launch) — [VGChartz](https://www.vgchartz.com/article/450825/potion-craft-sales-top-100000-in-3-days-on-steam/). Sensor Tower estimate: 1.3M units and ~$14.8M revenue — [Sensor Tower](https://app.sensortower.com/vgi/game/potion-craft-alchemist-simulator)

**Opus Magnum / Zachtronics**
- Opus Magnum: any working solution advances the player. Leaderboards challenge them to build the fastest, cheapest, or smallest machine — [Wikipedia (via search)](https://en.wikipedia.org/wiki/Opus_Magnum)
- Exapunks: solutions are scored on cycles, code size, and activity. Scores are shown against other players via histograms and friend leaderboards — [Wikipedia (via search)](https://en.wikipedia.org/wiki/Exapunks)
- Zachtronics announced its closure in June 2022, after Last Call BBS and a solitaire collection. Barth said the team was locked into making "Zachtronics games" — [PC Gamer](https://www.pcgamer.com/why-last-call-bbs-is-the-last-call-for-indie-studio-zachtronics/); [80.lv](https://80.lv/articles/puzzle-studio-zachtronics-announces-its-closure). Barth's successor studio, Coincidence, released Kaizen: A Factory Story in July 2025 — [GamesRadar](https://www.gamesradar.com/games/simulation/make-games-and-die-thats-my-plan-coincidences-zach-barth-on-making-games-about-making-things-a-year-of-teaching-and-being-in-it-for-the-long-haul/)

**Doodle God / Little Alchemy / Infinite Craft**
- Doodle God: Infinite Craft 3D has 5M+ Google Play downloads — [Google Play](https://play.google.com/store/apps/details?id=joybits.doodlegod_hd_blitz&hl=en_US). AppBrain estimates 7.1M lifetime downloads — [AppBrain](https://www.appbrain.com/app/doodle-god-alchemy-simulator/joybits.doodlegod_hd_blitz)
- Infinite Craft (Neal Agarwal, Jan 31 2024): the launch post drew 15M+ views in one week — [Know Your Meme](https://knowyourmeme.com/memes/sites/infinite-craft). The creator reported "200,000 unique combinations tried so far!" on launch day — [Prima Games](https://primagames.com/tips/how-many-possible-combinations-are-there-in-infinite-craft-answered)

### Inferences (loop breakdowns — analyst synthesis from the cited mechanics; not quoted from sources)
Schema: core action → immediate feedback → resource/reward → spend/invest → new capability → back; time scale; dominant effort.

| Game | Core action | Immediate feedback | Resource / reward | Spend / invest | New capability | Time scale | Dominant effort |
|---|---|---|---|---|---|---|---|
| Outer Wilds | Fly, explore, read Nomai text within a 22-min loop | Ship-log fact added; "more to explore" flag | Facts (rumor → explored) | Spend the next loop on a hypothesis or route | Reach a knowledge-gated location (e.g., timing, a quantum rule) | 22-min loop; 2–5-hr arcs | Insight |
| Baba Is You | Push word blocks to rewrite rules | Rules re-evaluate instantly; undo is free | Solved level → map nodes | Choose which branch to attempt | Learned rule-interaction idioms (meta-tricks) | Seconds of action, minutes to hours per insight | Insight |
| Obra Dinn | Visit death memories; inspect clues | Fates confirmed in batches (batch size not verified this session — see Gaps) | Confirmed identities | Use confirmed facts to eliminate others | Narrowed solution space | Minutes per fate; ~10-hr arc | Insight / deduction |
| The Witness | Draw a line on a panel | Panel lights or fails | Panel/area completion; power cables | Choose an area | Internalized symbol rule, which transfers to the environment | Seconds to minutes per panel | Insight |
| Tunic / Fez / Animal Well | Explore, observe the world and manual/glyphs | Hidden interaction triggers | Secret / page / cube / egg | Apply decoded language or rule | Reinterpret the already-seen world ("second layer") | Hours; community-scale for meta-secrets | Insight, plus skill (Tunic) |
| Heaven's Vault | Translate glyphs by guessing | Later confirmation of translations | Lexicon entries | Apply words to new inscriptions | Faster translation, more story | Minutes per inscription | Insight |
| Opus Magnum / Infinifactory | Build a machine | Simulation runs; pass/fail | Solved puzzle + metrics (cost/cycles/area) | Optimize vs. histogram | Better personal technique | Minutes to hours | Insight + optimization |
| Magicka | Combine up to 5 elements into a spell | Spell effect visible immediately | Discovered combos (Magicks) | Use in combat | Expanded spell repertoire | Seconds | Skill + experimentation |
| Little Alchemy / Doodle God / Infinite Craft | Combine two items | New item or nothing | New element in a collection | Combine new item further | Larger combinatorial frontier | Seconds | Time / brute force + insight |
| Potion Craft | Grind and mix ingredients; navigate the alchemy map | Position on map; effect reached | Potions sold → gold | Buy ingredients/upgrades | New map regions/recipes; save recipe | Minutes; day cycle | Time + insight |
| Cultist Simulator | Slot cards into verbs | Timer resolves into new cards/text | Lore, funds, followers | Feed into rituals/studies | New verbs/aspects/endings | Real-time minutes; runs of hours | Insight + risk |

- The common structure is a **zero-cost or near-zero-cost probe** (undo in Baba, a loop reset in Outer Wilds, a single combine in Little Alchemy) plus **legible state change**. That pairing lets players test hypotheses cheaply.

### Gaps
- Steam review scores and counts, SteamDB peak/current CCU, achievement completion percentages, HowLongToBeat times, and Metacritic scores could not be retrieved for any title except partial Outer Wilds review data. Steam, Steam Community, and Wikipedia were unreachable from this environment. **The report-writer should not cite specific HLTB/Metacritic/achievement figures from these notes.**
- No sales data found for Baba Is You, Heaven's Vault, Infinifactory, Opus Magnum, Magicka, or Little Alchemy (official). Obra Dinn's mechanic of confirming fates in batches was not confirmed by a retrieved source.
- No transcript of the Outer Wilds GDC 2020 talk, Teikari's GDC talk, or Barth's design talks was retrieved.

## Q2. How insight is rewarded; what makes "aha" land vs. frustrate

### Takeaway
Designers deliberately let players get confused before the "aha", then use structured breadcrumbs to stop confusion becoming abandonment. Examples are Outer Wilds' Rumor Mode and Cultist Simulator's late-added hints. The insight itself is the reward: knowledge, not stats, unlocks progress. Frustration arises when the designer misjudges difficulty (Teikari's "blindness") or when opacity offers no partial-progress signal.

### Cited Findings
- Kennedy (Cultist Simulator): "If the game had been more straightforward, it would have been much less interesting, but early versions were so opaque as to be almost unplayable." "Aha!" moments are most exciting after confusion, but "confused players lose patience very quickly." He added hints when players had part of a solution, and breadcrumbs "obscure enough that they didn't undermine the rest of the game's design, but apparent enough to lead all players usefully from objective to objective" — [Kennedy, "The Way through the Wood"](https://medium.com/@alexiskennedy/alexis-kennedy-on-cultist-simulator-the-way-through-the-wood-part-5-df3fc2459780); [Game Developer retrospective](https://www.gamedeveloper.com/business/cultist-simulator-the-retrospective)
- Blow (The Witness): it is "not just about the solving of problems, but what happens when you do". The game models "the feeling of epiphany with great care" — [Game Developer](https://www.gamedeveloper.com/design/-i-the-witness-i-modeling-epiphany)
- Beachum (Outer Wilds): about three clues per Curiosity, spread across planets. Progress is purely knowledge-gated — [Medium interview](https://medium.com/@cordialkobold/interview-with-alex-beachum-creative-director-of-outer-wilds-a01bb9631e20)
- Rumor Mode visualizes relationships between pieces of information to guide players — [Cuthbertson PDF](https://paigecuthbertson.com/pdfs/The_Ship_Log_in_Outer_Wilds.pdf?target=%22_blank%22). The "There's more to explore here" flag tells players a location is not exhausted — [Steam guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3500382207)
- Teikari: a solo developer becomes blind to difficulty, so "too easy" puzzles proved very hard. There is a lot of underlying logic beneath a simple concept — [MCV/DEVELOP](https://mcvuk.com/development-news/when-we-made-baba-is-you/)
- SpaceChem design: each puzzle was made "logically unique" so it "could not be solved by repeating a previous solution", without the team knowing all solutions in advance — [Game Developer SpaceChem postmortem](https://www.gamedeveloper.com/design/postmortem-zachtronics-industries-i-spacechem-i-)
- Animal Well: the ARG response showed players value secrets. Basso designed for a casual majority plus a hardcore layer — [Game Developer](https://www.gamedeveloper.com/design/why-animal-well-s-home-brewed-engine-was-key-to-its-success)

### Inferences
- What makes the "aha" land: (1) the rule was observable beforehand, so the insight re-reads existing evidence; (2) testing it is cheap; (3) the game confirms progress externally (a log entry, a lit panel, a batch confirmation); (4) partial progress is signaled.
- What causes frustration: no partial signal; probes that are expensive or slow; designer blind spots in the difficulty curve.
- For a natural-science sandbox, an Outer Wilds-style "recipe log" with rumor vs. confirmed facts maps directly onto hypothesis vs. verified law.

### Gaps
- No quantitative stuck/abandonment data (e.g., achievement drop-off curves) was retrievable.

## Q3. The replayability problem and mitigations

### Takeaway
Pure knowledge games have weak replay value once solved. Outer Wilds players speak wistfully of "wiping their memory", and the game can be finished in under 30 minutes with full knowledge. Mitigations that work: optimization metrics and histograms (Zachtronics), user-shared solutions, layered secrets and community meta-puzzles (Fez, Tunic, Animal Well), and seeded randomization of rules (Noita, roguelike ID).

### Cited Findings
- Outer Wilds Steam forum posts:
  - "I really wish I could wipe my memory of it so I could experience it again for the first time" — [Steam discussion](https://steamcommunity.com/app/753640/discussions/0/598531176428279474/)
  - About 20 hrs blind to full knowledge, after which the game is short. Players suggest waiting 1–2 years to forget — [Steam "Replay value?"](https://steamcommunity.com/app/753640/discussions/0/2518023667589574178/)
  - A new game to the end credits in under 30 minutes is possible, and there is an achievement for finishing in the first loop — [same thread](https://steamcommunity.com/app/753640/discussions/0/2518023667589574178/)
  - Deleting a save mainly removes the ship log, because progress lives in the player's head — [Steam discussion](https://steamcommunity.com/app/753640/discussions/0/2518023667592336699?l=latam)
- Beachum: "if you know everything, you can just boop-da-boop-da-boop" — [Medium](https://medium.com/@cordialkobold/interview-with-alex-beachum-creative-director-of-outer-wilds-a01bb9631e20). Outer Wilds was originally conceived as a roguelike with randomized elements — [podcast](https://open.spotify.com/episode/0iuocjlbq4hWDV7B0y3smJ)
- Zachtronics' optimization culture began accidentally. Barth's Flash games saved solutions as text, so players competed in Kongregate comments to build the most efficient solutions — [SpaceChem postmortem](https://www.gamedeveloper.com/design/postmortem-zachtronics-industries-i-spacechem-i-). Exapunks and Opus Magnum later formalized this with histograms and leaderboards — [Exapunks](https://en.wikipedia.org/wiki/Exapunks); [Opus Magnum](https://en.wikipedia.org/wiki/Opus_Magnum). Players describe hyper-optimized solutions, including manual loop unrolling for leaderboard entries — [MetaFilter](https://www.metafilter.com/184009/coding-chemistry-mechanization-and-alchemy)
- Infinite Craft: an emergent "First Discovery" mechanic and social sharing of crafted results kept virality going. One Feb 1 2024 post got 2.8M+ views in four days — [Know Your Meme](https://knowyourmeme.com/memes/sites/infinite-craft); [Twinfinite](https://twinfinite.net/guides/is-infinite-craft-actually-infinite/)

### Inferences
- Histograms turn a binary "solved" into a continuous skill target, which gives a solved puzzle a second life. A natural-science sandbox could score "recipes" on efficiency, yield, and cost against a distribution.
- Randomized constants (the user's planned mode) directly address the Outer Wilds problem. Methods (how to probe) stay valuable even when facts (specific values) reset. This mirrors expert play in roguelike ID systems (see Q4).

### Gaps
- No retention or return-rate data (e.g., SteamDB CCU long tails) was retrieved for any title.

## Q4. Games that randomize rules per playthrough, and how players respond

### Takeaway
Rule randomization per run is well established: Rogue/NetHack item identification and Noita's per-seed alchemy recipes. Players value the tension and the "lucky unknown item" moments. They dislike tedious ID rituals and spoiler-driven play, and they quickly build external tools that compute seed recipes. Randomizing only a few high-value rules (as Noita does) keeps most knowledge stable.

### Cited Findings
- Noita: only two recipes (Lively Concoction, Alchemic Precursor) are randomized per world seed. Each uses three materials: a 25% chance of 3 liquids, 75% of 2 liquids + 1 powder. The recipes do not change in NG+ — [Noita Wiki: Alchemy](https://noita.wiki.gg/wiki/Alchemy); [dood.gg alchemy guide](https://dood.gg/en/noita/guides/alchemy/)
- The recipes are mostly discovered by chance, and their distinctive colors make them noticeable — [Noita Wiki: Alchemic Precursor](https://noita.wiki.gg/wiki/Alchemic_Precursor). Players built seed-to-recipe calculators and in-game mods — [Neff's recipe generator](https://neffc.github.io/narg/); [Zatherz LC&AP](https://zatherz.github.io/noita/)
- Rogue/NetHack: item appearances reshuffle each game. Identification must be scarce and uncertain enough that waiting has a cost — [Game Developer @Play 81](https://www.gamedeveloper.com/design/-play-81-on-rogue-s-item-identification-system)
- Criticisms:
  - Price-identification in shops is called the "worst offender" — [Golden Krone Hotel dev blog](https://www.goldenkronehotel.com/wp/2017/06/25/things-i-hate-about-roguelikes-part-2-identification/)
  - Workaround tricks become spoilers and tedium, "game after game" — [Golden Krone Hotel](https://www.goldenkronehotel.com/wp/2017/06/25/things-i-hate-about-roguelikes-part-2-identification/)
  - Proposals include showing a small set of possible identities on inspection — [NetHack idea tracker](https://nethack-yanis.github.io/tag/identification)
- The defense: quaffing an unknown potion at the last hitpoint and surviving "feels amazing" and creates memorable deaths — [Golden Krone Hotel](https://www.goldenkronehotel.com/wp/2017/06/25/things-i-hate-about-roguelikes-part-2-identification/)
- The community maintains formal ID spoilers — [NetHack Object Identification Spoiler](https://www.chiark.greenend.org.uk/~damerell/games/nhid.html)

### Inferences
- If randomized world constants are deterministic from the seed, players will reverse-engineer and tool them (as with Noita). Consider server-side seeds or non-shareable variation if relearning is the point. Alternatively, embrace community tooling as engagement.
- Offer in-world measuring instruments and a "possible values" UI (the Golden Krone approach). This avoids ID-style tedium while keeping relearning meaningful.

### Gaps
- No source on how Cultist Simulator randomizes per run. Its rules are fixed; only draws vary, and that was not verified here. No player-sentiment numbers (e.g., review-text frequencies) were found.

## Q5. How recipe/combination-discovery systems perform

### Takeaway
Combination games have high reach: Doodle God has 5M+ downloads on one listing, and Infinite Craft went viral in 2024. Potion Craft sold strongly at 100k in 3 days. Minecraft eventually added a recipe book (1.12, 2017) that unlocks recipes as materials are gathered. This suggests that pure blind discovery needed a recording/assist layer at mass scale.

### Cited Findings
- Doodle God: Infinite Craft 3D has 5M+ Google Play installs and an AppBrain estimate of 7.1M — [Google Play](https://play.google.com/store/apps/details?id=joybits.doodlegod_hd_blitz&hl=en_US); [AppBrain](https://www.appbrain.com/app/doodle-god-alchemy-simulator/joybits.doodlegod_hd_blitz)
- Infinite Craft: 15M views on the launch post in one week; 200k unique combinations tried on launch day. Some combinations "refuse" and default to one input — [Know Your Meme](https://knowyourmeme.com/memes/sites/infinite-craft); [Prima Games](https://primagames.com/tips/how-many-possible-combinations-are-there-in-infinite-craft-answered); [Twinfinite](https://twinfinite.net/guides/is-infinite-craft-actually-infinite/)
- Potion Craft: 100k+ Steam units in 3 days; 1.3M units estimated by Sensor Tower — [VGChartz](https://www.vgchartz.com/article/450825/potion-craft-sales-top-100000-in-3-days-on-steam/); [Sensor Tower](https://app.sensortower.com/vgi/game/potion-craft-alchemist-simulator)
- Minecraft: the recipe book was introduced in 1.12 (June 2017), tied to advancements. Recipes unlock as players gather materials — [Craftdex](https://craftdex.net/articles/the-recipe-book-and-unlocks); [Minecraft Wiki](https://minecraft.wiki/w/Furnace_recipe_book); [G-Portal](https://www.g-portal.com/wiki/en/the-minecraft-recipe-book/)

### Inferences
- Combination discovery attracts broad casual reach, but it tends toward brute-force enumeration (time effort) unless the combination space is governed by learnable rules (insight effort). A science sandbox should make results predictable from underlying properties, so recipes are inferable rather than memorized.
- The auto-recording recipe book is an accessibility layer. It keeps the reward (discovery) while removing tedium (re-memorizing). The user's planned "record recipes" feature parallels Minecraft's recipe book and Potion Craft's recipe saving.

### Gaps
- No primary player-sentiment data on Minecraft's pre-1.12 discovery or reaction to the recipe book. No official download totals for Little Alchemy 1/2. Magicka element-combination player reception was not researched due to the tool budget.
