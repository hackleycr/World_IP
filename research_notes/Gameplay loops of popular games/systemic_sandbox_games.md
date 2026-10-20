# Gameplay Loops of Systemic / Sandbox / Simulation Games

Research date: 2026-10-20. **Method caveat (read first):** In this environment the egress proxy refused direct access to store.steampowered.com, api.steampowered.com and steamcharts.com, and WebFetch could not resolve those hosts. SteamDB and HowLongToBeat pages were not fetched either. Every figure below therefore comes from web-search results that quote press, developer statements or third-party trackers. Each figure carries the date of its source (or "undated snapshot"). Where a figure is only a third-party estimate (VG Insights, Boxleiter, SteamPulse, Raijin, Vaporlens), it is labelled as one. **Live "recent concurrent players" for October 2026 could not be collected for any game.** Treat that as an open gap and check SteamDB by hand.

Loop breakdowns use the requested schema (core action -> immediate feedback -> resource/reward -> spend/invest -> new capability -> back to core action). They are analyst syntheses built from the cited design statements and reviews, so they are labelled **[synthesis]**. They are not quoted from any one source.

---

## Q1. Which loop features recur across the most successful and long-lived sandbox games? (includes per-game breakdowns and signals)

### Takeaway
The longest-lived games here are Minecraft, Terraria, Factorio and RimWorld. Each pairs a short tactile loop measured in seconds (dig, place, shoot, build) with an open-ended long-term loop whose goals the player sets, rather than a scripted endpoint. Each also has a rule set that players can learn, so rules interact in combinations the developers did not script. Developers say outright that they design for this: Nintendo calls it "multiplicative" design, Ludeon calls RimWorld a "story generator", and Bay 12 says "there is no win condition".

### Cited Findings

#### Noita (Nolla Games; full release Oct 2020)
- **Loop [synthesis]:** explore a fully simulated pixel world and cast spells (seconds) -> materials burn, melt, flow and explode visibly at once -> gold, new wands, spells and perks (minutes) -> edit wands at Holy Mountain checkpoints by arranging spells (minutes) -> stronger or stranger wand behaviour, including self-destructive builds -> descend deeper (run, about 1 session; meta-knowledge of secrets is long-term). Dominant effort: **insight + risk**. Knowledge carries over between runs but power does not.
- Every pixel in the world is simulated. Developers describe it as cellular automata following simple local rules (for example, a liquid checks whether it can fall, then whether it can slide sideways) — [80.lv](https://80.lv/articles/noita-a-game-based-on-falling-sand-simulation/); [Wikipedia](https://en.wikipedia.org/wiki/Noita_(video_game))
- Petri Purho said the real difficulty was game design, not tech: "technical questions are easier to settle" (paraphrase) — [Game Developer, Road to the IGF](https://www.gamedeveloper.com/game-platforms/road-to-the-igf-nolla-games-i-noita-i-)
- The GDC 2019 talk "Exploring the Tech and Design of Noita" (Petri Purho) exists and is linked from community forums. Its content could not be fetched — [io-tech forum](https://bbs.io-tech.fi/threads/noita-pc.106023/)
- **Sales:** no official figure was found. Third-party estimates: about 2.6M units / $35M (SteamPulse, VGI method, undated snapshot) — [SteamPulse](https://steampulse.org/game/881100). About 3.24M copies (Boxleiter-style estimate from review count, undated) — [Steam Page Analyzer](https://www.steampageanalyzer.com/tools/revenue-calculator/881100)
- **Concurrent players:** SteamPulse lists an all-time peak of 3,045 and 2,221 "playing now" (undated snapshot). The search tool flagged the peak as implausibly low for about 80k+ reviews, so treat it as **unverified** — [SteamPulse](https://steampulse.org/game/881100)
- **Praised:** wand modification is "one of the core facets of this wonderful, maddening roguelike". PC Gamer score 81 — [PC Gamer review](https://www.pcgamer.com/noita-review/). Hundreds of hidden secrets, "some of which you probably won't run into even after spending hundreds of hours", and 307 spells at time of review — [Bonus Stage](https://www.bonusstage.co.uk/tag/noita/)
- **Criticised:** instant deaths from your own spells ("no safety net if that experimentation goes awry") — [PC Gamer](https://www.pcgamer.com/noita-review/). Survival depends on luck in finding wands and spells, and enemies have "pinpoint accuracy" — [GOG user reviews](https://www.gog.com/game/noita). The early game is a "sleep-inducing slog if a better weapon isn't found immediately" — [Steam discussion](https://steamcommunity.com/app/881100/discussions/0/3159763879055769749)

#### Minecraft (Mojang/Microsoft)
- **Loop [synthesis]:** mine or place a block (seconds) -> block breaks or appears, item drops -> raw materials -> craft tools, furnaces, shelter -> deeper mining, new biomes, redstone and automation -> build or explore. Long-term goals are set by the player (megabuilds, redstone machines, the Ender Dragon). Dominant effort: **time early, insight late (redstone)**.
- The tight loops are mining, crafting tools, building shelter and surviving mobs. Larger arcs such as building a castle or defeating the Ender Dragon emerge from the player rather than being scripted (blog analysis, 2025-05-14) — [Mechanics of Magic](https://mechanicsofmagic.com/2025/05/14/sketchnote-loops-arcs-32/)
- Notch built "a world with very specific rules" and simple mechanics with "no one solution to each situation" (2015, secondary) — [Social Media Today](https://www.socialmediatoday.com/technology-data/2015-04-05/emergence-and-gamification-learning-love-unintentional)
- Redstone behaves like electrical circuitry, and players build calculators and computers from it — [Peachpit, "Redstone: The Charge That Ignites Minecraft"](https://peachpit.com/articles/article.aspx?p=2324462); [Metavert](https://metavert.io/emergent-gameplay)
- **Sales/MAU:** about 350M lifetime by about April 2025, and passed 300M at Minecraft Live 2023. About 212M MAU in 2025, peaking around 222.5M in June 2025 after the film. Microsoft no longer publishes regular MAU, so these are **third-party aggregations, not audited** — [HostHavoc stats (updated 2026-05-18)](https://hosthavoc.com/blog/minecraft-statistics). Conflicting: about 325M in early 2025 — [SQ Magazine](https://sqmagazine.co.uk/minecraft-statistics/)
- Not on Steam, so no Steam review or CCU data exists.

#### Terraria (Re-Logic)
- **Loop [synthesis]:** dig, fight, explore in 2D (seconds) -> loot and ore drops, enemy death -> ores, boss drops -> craft gear at crafting stations and build NPC housing -> new tier unlocks the next biome or boss (bosses gate progression) -> deeper exploration. Session-to-long-term arc runs pre-Hardmode -> Hardmode -> Moon Lord. Dominant effort: **time + skill**, with insight needed for crafting trees, which are often learned from the wiki.
- **Sales:** 70M copies as of May 2026 (39.6M PC, 19.7M mobile, 10.7M console), announced for the 15th anniversary — [Massively OP, 2026-05-20](https://massivelyop.com/2026/05/20/legendary-multiplayer-sandbox-terraria-celebrates-15-years-of-live-service-with-over-70m-copies-sold). Earlier: 58.7M in mid-2024, about 32M on PC — [Time Extension, 2024-07](https://www.timeextension.com/news/2024/07/we-passed-a-somewhat-obscure-game-about-a-plumber-terraria-overtakes-super-mario-bros)
- **Playtime:** HowLongToBeat averages 106 h to beat and 205 h for completionists (HLTB tweet, 2026) — [HowLongToBeat on X](https://x.com/HowLongToBeat/status/2031392204363546951)
- Steam review count, score and CCU peak: **not retrieved** (gap).

#### Dwarf Fortress (Steam edition, Bay 12 / Kitfox; Steam release 2022-12-06)
- **Loop [synthesis]:** designate dig, build and work orders (minutes, indirect control) -> dwarves carry out jobs and announcements report events -> stone, ore, food, crafted goods, wealth -> workshops, defences, industry, nobles -> bigger fortress draws migrants, sieges and megabeasts -> new crises. Long term: the fortress falls ("Losing is fun"), then a new embark in a world with persistent history. Dominant effort: **insight** (deep, poorly surfaced rules) **+ time**.
- 160,000+ sales in the first 24 hours (Kitfox) — [Game World Observer, 2022-12-13](https://gameworldobserver.com/2022/12/13/dwarf-fortress-300k-units-sold-zach-tarn-adams-millionaires). Passed 800,000 Steam sales "in just over a year" (Adams brothers to PC Gamer, early 2024) — [Game Developer](https://www.gamasutra.com/business/dwarf-fortress-has-topped-800-000-sales-in-just-over-a-year)
- **Design intent:** the help manual's motto is "Losing is fun!". "If you're bored, you win." "There is no win condition" — [Jackson Free Press, 2013-04-24](https://www.jacksonfreepress.com/news/2013/apr/24/joy-failure/). "It's important that people learn to embrace loss, or the world can't be enriched by their passing" — [Technical.ly, 2014-05-21](https://technical.ly/brooklyn/2014/05/21/dwarf-fortress-adams/). The game simulates a whole world, its history and people, and personalities are built from deeper models because modern psychological categories were "too simplistic" — [Technical.ly](https://technical.ly/brooklyn/2014/05/21/dwarf-fortress-adams/); [Software Engineering Daily, 2015-10-22](https://softwareengineeringdaily.com/2015/10/22/dwarf-fortress-with-tarn-adams)
- Steam review score, count and CCU: **not retrieved** (gap).

#### Teardown (Tuxedo Labs / Saber)
- **Loop [synthesis]:** destroy and rearrange the voxel world with tools, explosives and vehicles (seconds) -> fully physical destruction you can see -> mission cash and tool upgrades -> plan a heist route by pre-cutting walls and staging vehicles before the alarm timer (minutes) -> new tools and levels -> next heist. The sandbox mode and mods (Steam Workshop) carry the long term. Dominant effort: **insight (route planning) + skill**.
- 1.1M copies by Aug 2022, which led to Saber's acquisition of the studio. 2.5M players across platforms after the PS5/Xbox launch on 2023-11-15 (official, late Nov 2023) — [Game Developer press release](https://gamedeveloper.com/press-release/-teardown-smashes-past-2-5-million-players-); [Wikipedia](https://en.wikipedia.org/wiki/Teardown_(video_game))
- Early Access launch (Oct 2020) rated "Overwhelmingly Positive" from more than 35,000 reviews at the time; a peak of 15,068 over two weeks (undated ITAD snapshot) — [IsThereAnyDeal](https://isthereanydeal.com/game/teardown/info/). Unverified fan claim of 2.7M Steam sales — [levvvel](https://levvvel.com/teardown-statistics/)

#### The Legend of Zelda: Breath of the Wild (Nintendo, 2017)
- **Loop [synthesis]:** traverse, climb, glide and interact with physics or chemistry (seconds) -> fire spreads, wind blows, metal conducts, objects tumble -> shrines (Spirit Orbs), Korok seeds, materials, weapons -> hearts and stamina, inventory slots, cooking, armour upgrades -> reach new areas and attempt harder fights -> see a tower or landmark and go there. Dominant effort: **insight + exploration time**. Weapon durability adds risk.
- **Design intent (GDC 2017, "Breaking Conventions with The Legend of Zelda: Breath of the Wild"):** Fujibayashi moved from "additive" design (objects act independently) to "multiplicative" design (objects react to the player and to each other). The aim was "active" rather than "passive" play, replacing predetermined puzzle solutions. Dohta described a Havok physics engine plus a separate "chemistry engine" of rules for elements (fire, ice, wind). The team prototyped multiplicative mechanics in a 2D recreation of the original NES Zelda — [Thumbsticks GDC17](https://www.thumbsticks.com/gdc-17-breaking-conventions-breath-of-the-wild); [Zelda Universe, 2017-03-09](https://zeldauniverse.net/2017/03/09/zelda-team-discusses-breath-of-the-wilds-development-and-2d-zelda-prototype-at-gdc/); [TechRadar](https://www.techradar.com/news/zelda-breath-of-the-wilds-creators-prototyped-with-the-original-nes-classic). The physics system tells "clever lies" so it stays controllable rather than realistic — [Thumbsticks](https://www.thumbsticks.com/gdc-17-breath-of-the-wild-science-lies)
- **Sales:** about 31.61M–31.85M units (reports around late 2024; sources differ slightly). No confirmed 2025/2026 figure was found — [Siliconera](https://siliconera.com/?p=1027648)
- **Metacritic:** 97 (Switch) — [Prima Games](https://primagames.com/?p=124240). Switch 2 edition reported as 95 by one source and 93 by another — [NME](https://www.nme.com/news/gaming-news/the-best-reviewed-games-of-2025-so-far-zelda-mario-3876796)

#### The Legend of Zelda: Tears of the Kingdom (Nintendo, 2023)
- **Loop [synthesis]:** BotW loop plus Ultrahand, Fuse and Autobuild. Grab and attach parts (seconds) -> the contraption moves, flies or fails physically -> Zonai devices, materials, shrine rewards, Zonaite -> battery upgrades, saved Autobuild schematics -> larger vehicles and new traversal solutions -> explore the sky and depths. Dominant effort: **insight + creativity**. Autobuild works as a reusable "recipe".
- **Design intent:** Fujibayashi first prototyped Ultrahand by building vehicles from BotW's existing parts and showing them to the team — [Nintendo "Ask the Developer" vol. 4](https://www.nintendo.com/sg/interview/totk/04.html). The game's crux is Ultrahand and "the freedom to create" (Game Informer via secondary source). Simplicity and legibility were key to adoption (Game Maker's Toolkit analysis). "No one correct way to clear a puzzle" (Famitsu). Dohta: the team spent much effort tuning object combinations and wants players to "experiment with lots of combinations and find their favorite" — [GoNintendo](https://www.gonintendo.com/contents/29652-zelda-tears-of-the-kingdom-team-discusses-the-ultrahand-s-key-role-and-their-focus); [Zelda Dungeon](https://www.zeldadungeon.net/informative-new-video-analyzes-how-nintendo-designed-ultrahand-for-tears-of-the-kingdom/)
- The director said community Ultrahand builds went beyond what the team imagined — [Zelda Universe, 2024-06-05](https://zeldauniverse.net/2024/06/05/tears-of-the-kingdom-director-and-producer-reflect-on-the-games-first-year/). Players built record-length objects, Podracers and Lynel-killing tanks, and a fan site ("Zelda Builds") formed to share designs — [Zelda Universe, 2024-04-02](https://zeldauniverse.net/2024/04/02/tears-of-the-kingdom-creation-boasts-games-longest-object/); [Boss Rush, 2024-05-11](https://bossrush.net/2024/05/11/a-comprehensive-look-at-one-year-of-the-legend-of-zelda-tears-of-the-kingdom/)
- **Sales:** 10M in 3 days (May 2023); 18.51M by end of June 2023 — [RPG Site](https://www.rpgsite.net/news/14591-nintendo-q1fy2024-results-the-legend-of-zelda-tears-of-the-kingdom-sells-1851-million-units); 20.28M as of 2023-12-31 — [Shacknews](https://shacknews.com/article/138620/nintendo-ntdoy-zelda-totk-20-million?amphtml=1). "Passed 21M by March 2025" appears only secondhand (unverified).
- **Metacritic:** 96 at launch. OpenCritic 97, its highest-rated game at the time — [Prima Games](https://primagames.com/news/the-legend-of-zelda-tears-of-the-kingdom-metacritic-score-revealed); [Press Start, 2023-05-12](https://press-start.com.au/news/nintendo/2023/05/12/the-legend-of-zelda-tears-of-the-kingdom-is-already-opencritics-highest-rated-game-ever/amp/)

#### Factorio (Wube Software)
- **Loop [synthesis]:** place miners, belts, inserters, assemblers (seconds) -> items flow visibly and bottlenecks show up -> science packs -> research -> new recipes and machines (oil, trains, robots, logistics) -> redesign and scale up. Blueprints let you copy-paste solved designs. Long term: rocket, then the "factory must grow" megabase; Space Age adds planets. Dominant effort: **insight (layout and ratio puzzles)**, followed by **time**.
- **Praised:** "Setting up the assemblers, belts, and inserters is always a wonderful puzzle to solve, and watching the line kick into motion is hugely gratifying." Goals evolve "from the player's own ideas" — [Windows Central review](https://windowscentral.com/factorio-pc-review); [bit-tech](https://bit-tech.net/reviews/factorio-review/1/)
- **Criticised:** a steep learning curve ("dauntingly complex", IGN via aggregator), plain visuals, small problems hard to spot from the top-down view — [GameGeeker](https://gamegeeker.com/games/factorio/review?country=US); [bit-tech](https://bit-tech.net/reviews/factorio-review/1/)
- **Player view (forum opinion, not dev):** "the factory must grow" is a by-product of scale mechanics, and megabases are "benchmarking" with no new problems — [Factorio forums, FFF #365 thread](https://forums.factorio.com/viewtopic.php?p=536611)
- **Sales/CCU:** Space Age sold 400k+ copies at launch (Wube, FFF, Oct 2024). CCU peak of 118,674 at Space Age launch versus 34,700 in 2020 — [GamingOnLinux, 2024-10](https://gamingonlinux.com/2024/10/factorio-space-age-sold-over-400000-copies-and-sets-a-new-player-count-record). Cumulative "5M+" comes only from an aggregator, not Wube — [GameGeeker](https://gamegeeker.com/games/factorio/review?country=US)
- **Scores:** Steam about 97% positive, Metacritic 90 (aggregator, undated) — [GameGeeker](https://gamegeeker.com/games/factorio/review?country=US)
- **Playtime:** about 200+ h for all achievements (TrueSteamAchievements, 34 users) — [TSA](https://truesteamachievements.com/game/Factorio/completiontime)

#### Oxygen Not Included (Klei)
- **Loop [synthesis]:** queue dig, build and duty orders for duplicants (seconds to minutes) -> gas and liquid overlays show O2, CO2, heat and germs spreading -> food, oxygen, power, refined materials -> build machines, plumbing, automation wiring, research -> stable closed-loop systems (power, water, heat) -> expand, then the next crisis (overheating, starvation) -> rebuild. Dominant effort: **insight (thermo, fluid and gas physics) + risk**.
- **Reviews:** 97% positive of 140,190 (SteamPulse, undated); 96.8% of 139,277, "Overwhelmingly Positive" (Vaporlens, undated) — [SteamPulse](https://steampulse.org/game/457140); [Vaporlens](https://vaporlens.app/app/457140/oxygen_not_included/stats/details). Metacritic 85 (aggregator) — [GameGeeker](https://gamegeeker.com/games/oxygen-not-included-457140?market=PL)
- **Sales:** no official figure. About 3.2M Steam estimate (Raijin, "medium confidence") — [Raijin](https://raijin.gg/app/457140/Oxygen_Not_Included). Tracked CCU peak about 27,380 (SteamPulse) — [SteamPulse](https://steampulse.org/game/457140)
- The Spaced Out! DLC went into Early Access on 2020-12-08 and left it on 2021-12-16 — [Klei forums](https://forums.kleientertainment.com/forums/topic/136216-oxygen-not-included-spaced-out-leaves-early-access/)

#### RimWorld (Ludeon)
- **Loop [synthesis]:** set priorities, zones and builds for colonists (minutes, indirect) -> colonists' moods, relationships and events show up as notifications -> food, silver, components, research -> buildings, defences, prosthetics, DLC systems -> stronger colony -> AI storyteller escalates raids and events -> drama and a new story beat. Long term: a run ends in escape or collapse, then a new colony. Dominant effort: **risk + insight**, with emotional investment in colonists.
- **Design intent:** GDC 2017 "RimWorld: Contrarian, Ridiculous, and Impossible Design Methods" frames RimWorld as a "story generator" rather than a game. Strategically omitted features let players fill gaps with their own story. Dwarf Fortress was the inspiration for its story generation — [GDC Vault](https://gdcvault.com/play/1024232/-RimWorld-Contrarian-Ridiculous-and); [GDC news](https://gdconf.com/news/gdc-youll-see-rimworld-devs-succeeded-everything-wrong). The title screen subtitle is "A story generator by Tynan Sylvester" — [Habrador blog, 2019-06](https://blog.habrador.com/2019/06/why-rimworld-sold-more-than-1-million.html)
- **Sales:** 1M+ (Sylvester, older statement; the Kickstarter targeted about 1,000) — [PCGamesN](https://www.pcgamesn.com/rimworld/rimworld-sales-numbers). About 11.1M estimate (Vaporlens, third-party, unverified) — [Vaporlens](https://vaporlens.app/app/294100/rim_world/stats/details)
- **CCU:** all-time peak 96,040 on 2025-07-20 (SteamDB, around the Odyssey DLC); SteamCharts lists 95,851 — [SteamDB](https://steamdb.info/app/294100/charts/); [SteamCharts](https://steamcharts.com/app/294100)
- **Playtime:** "60 to well over 300 hours" (Game Rant via search, secondary) — gap for HLTB.

#### Valheim (Iron Gate / Coffee Stain; EA Feb 2021)
- **Loop [synthesis]:** gather, fight and explore a biome (seconds to minutes) -> drops and boss trophies -> materials (wood, then bronze, iron, silver and so on) -> craft gear, upgrade workbench and forge, cook food buffs, build a base -> survive the next biome after a boss gate -> sail and explore. Dominant effort: **time (grind) + risk**. Co-op and base-building drive return play.
- **Sales:** 12M (Embracer AGM, Sep 2023); 10M (Apr 2022); 1M in its first week, 3M by day 16 — [Game Developer](https://gamedeveloper.com/business/-i-valheim-i-has-crafted-12-million-sold-copies); [Game World Observer, 2022-04-25](https://gameworldobserver.com/2022/04/25/valheim-surpasses-10-million-units-sold-in-14-months-since-its-launch)
- **CCU:** all-time peak about 502,387 on 2021-02-21 (Icon Era); 501,804 (Tracker.gg); 498,478 (SteamCharts). Trackers disagree slightly — [Icon Era](https://icon-era.com/statistics/valheim/); [Tracker.gg](https://tracker.gg/population/steam/892970); [SteamCharts](https://steamcharts.com/app/892970)
- **Criticised:** becomes "excessively grindy and tedious, especially after the initial biomes". Ashlands is "unbalanced, unplayable solo" and drives burnout (review-aggregator summary) — [Vaporlens](https://vaporlens.app/app/892970/valheim.md). Steam users split: "no real point except to reach the next tier" against "the grind is mostly about finding the places with the resources" — [Steam discussions](https://steamcommunity.com/app/892970/discussions/0/3494256256414828268)

#### Satisfactory (Coffee Stain; 1.0 on 2024-09-10)
- **Loop [synthesis]:** first-person: hand-gather, then place miners, constructors and belts (seconds) -> watch belts and factories run in 3D -> parts delivered to the Space Elevator and HUB milestones -> unlock tiers and alternate recipes (from hard drives found while exploring) -> new machines and logistics (trains, drones) -> rebuild and expand. Dominant effort: **insight (ratios, layout) + time**. Building aesthetics is a large secondary loop.
- **Sales:** 5M (Embracer, Sep 2023) — [Game Developer](https://gamedeveloper.com/business/-i-valheim-i-has-crafted-12-million-sold-copies)
- **CCU:** 1.0 launch peak of 104,677 (SteamDB via GWO), against a previous high of about 34,200 (Nov 2021). Later launch-window snapshots reported about 120k — [Game World Observer, 2024-09-11](https://gameworldobserver.com/2024/09/11/satisfactory-peaks-at-over-100k-ccu-launch); [Gamereactor](https://www.gamereactor.eu/satisfactory-topped-over-120000-concurrent-players-on-steam-1432173/)
- Praise and criticism: **not retrieved** (gap).

#### The Powder Toy and falling-sand games
- **Loop [synthesis]:** place an element with the brush (seconds) -> immediate reaction (burn, melt, conduct, explode) -> no resource economy. The "reward" is a new discovery or a saved creation -> share or upload saves and browse other people's -> more ambitious contraptions (electronics, reactors). Dominant effort: **insight / curiosity** only. No grind.
- Free, open-source. Released on Steam in June 2024, "Overwhelmingly Positive". 258 materials (as of Feb 2025) — [Wikipedia](https://en.wikipedia.org/wiki/The_Powder_Toy); [GamingOnLinux, 2024-06](https://gamingonlinux.com/2024/06/classic-free-physics-sandbox-game-the-powder-toy-is-now-on-steam/). Reviews: 2,813 (2,759 positive) per one listing, about 98% of 2,471 per another (undated) — [Vaporlens](https://vaporlens.app/app/1148350/the_powder_toy/stats/details)
- **Praised:** the physics engine and sandbox; players report thousands of hours. **Criticised:** "lack of traditional gameplay loops", missing materials, crashes, missing languages — [Vaporlens](https://vaporlens.app/app/1148350/the_powder_toy.md)
- Sandboxels (500+ elements, chemistry and life): 844 Steam reviews, 95% positive (undated, via a similarity list) — [Vaporlens](https://vaporlens.app/app/1148350/the_powder_toy.md)

### Inferences
- **Recurring features across the long-lived titles:**
  1. A seconds-scale action with instant, visible physical or systemic feedback (pixel sim, belts moving, blocks breaking).
  2. A legible rule set whose rules combine "multiplicatively".
  3. Unlocks that widen the space of possible actions rather than just raising numbers.
  4. Goals set by the player once scripted goals end (megabase, megabuild, colony story).
  5. Reusable artefacts that capture insight (blueprints, Autobuild, redstone designs, wand builds, Powder Toy saves) and support community sharing.
  6. Long post-launch update and DLC cycles that produce new CCU peaks years later: Factorio's peak in 2024 was 3.4x its 2020 peak, RimWorld's peak came in 2025, and Satisfactory's peak came at 1.0.
- Falling-sand toys show the limit of feature (2) alone. Without (3) and (4), players praise the physics but criticise the "lack of gameplay loops". For a 2D natural-science sandbox, Noita (sim + goals + run structure) and ONI (sim + survival pressure) are the closest commercial proofs that a pixel or fluid simulation can carry a full game.
- On "recent concurrent players": the pattern of DLC and 1.0 spikes suggests these games run as long-tail titles with periodic re-engagement. This could not be confirmed with October 2026 data.

### Gaps
- No October 2026 live or recent CCU for any game (Steam, SteamCharts and SteamDB were blocked).
- Steam review count and score were not retrieved for Terraria, Dwarf Fortress, Valheim, Satisfactory, RimWorld, Noita or Teardown (current). Only aggregator snapshots exist for Factorio, ONI and Powder Toy.
- Metacritic not confirmed for Noita, Terraria, Dwarf Fortress, Teardown, RimWorld, Valheim or Satisfactory.
- HowLongToBeat figures were found only for Terraria. Steam median playtime was not found for any game.
- Official sales are missing for Noita, ONI and a current Factorio total. No 2025/26 Nintendo totals for BotW or TotK were found.
- The contents of the Noita GDC talk could not be fetched. Only its existence is confirmed.

---

## Q2. How do these games handle grind versus insight, and how do players feel about it?

### Takeaway
Players reward games where progress is gated by **understanding** (Factorio, ONI, Noita, TotK) and complain where progress is gated by **repetition** (Valheim's later biomes, Noita's early luck-dependent runs). The most praised design converts grind into insight through automation: a player who has understood a system stops doing the work by hand.

### Cited Findings
- Factorio: building lines is "a wonderful puzzle", and watching them run is "hugely gratifying". Goals come from the player's own ideas — [Windows Central](https://windowscentral.com/factorio-pc-review)
- Factorio counter-view: megabases are "benchmarking" with "no new problems to solve" (player forum opinion) — [Factorio forums](https://forums.factorio.com/viewtopic.php?p=536611)
- Valheim: "excessively grindy and tedious, especially after the initial biomes" (aggregated review summary) — [Vaporlens](https://vaporlens.app/app/892970/valheim.md). Some players defend it: the game isn't grindy "unless you want fully upgraded gear or elaborate builds" — [Steam discussion](https://steamcommunity.com/app/892970/discussions/0/3494256256414828268)
- Noita: progress "depends on how lucky you are to find new wands and spells rather than your own skill" — [GOG reviews](https://www.gog.com/game/noita). The early game is a "slog" without a good wand, yet the same poster "deeply respects" the mid-to-late game — [Steam discussion](https://steamcommunity.com/app/881100/discussions/0/3159763879055769749)
- Dwarf Fortress reframes failure as content: "Losing is fun!" and "If you're bored, you win" — [Jackson Free Press](https://www.jacksonfreepress.com/news/2013/apr/24/joy-failure/)
- TotK: "no one correct way to clear a puzzle"; simplicity is a design principle so players embrace building — [GoNintendo](https://www.gonintendo.com/contents/29652-zelda-tears-of-the-kingdom-team-discusses-the-ultrahand-s-key-role-and-their-focus); [Zelda Dungeon](https://www.zeldadungeon.net/informative-new-video-analyzes-how-nintendo-designed-ultrahand-for-tears-of-the-kingdom/)
- The Powder Toy has zero grind but draws criticism for the "lack of traditional gameplay loops" — [Vaporlens](https://vaporlens.app/app/1148350/the_powder_toy.md)
- Steep learning curves (Factorio "dauntingly complex"; Noita "way too hard" even after watching others) are the most common complaint in insight-heavy games — [GameGeeker](https://gamegeeker.com/games/factorio/review?country=US); [Steam discussion](https://steamcommunity.com/app/881100/discussions/0/604148566876768427)

### Inferences
- There are two failure modes. "Grind without insight" (repeating gathering at a higher tier) causes burnout. "Insight without a goal" (pure sandbox) causes drift. Successful games sit between them: grind exists, but each new insight lets the player automate or skip it.
- For a recipe-writing design, recipes are the direct conversion of insight into reduced grind, the same role blueprints play in Factorio. The main risk is the onboarding cliff, which is the top complaint in Factorio, ONI and Noita.
- Randomness gating access to the expressive system (Noita's wands) causes frustration. Players want the toolkit available early and the challenge to come from using it.

### Gaps
- No quantitative player-sentiment split on grind (for example, the share of negative reviews mentioning grind). Steam review text could not be accessed.
- No sourced Satisfactory, ONI, Minecraft or Terraria player commentary on grind.

---

## Q3. How do emergent rule interactions and player-built systems drive long-term engagement?

### Takeaway
Player-built systems (redstone computers, Factorio blueprints and megabases, Ultrahand vehicles, Noita wands) turn a game into a medium for expression and sharing. Developers explicitly say communities go beyond their own designs, and the spikes in long-term engagement line up with expansions that add new rule sets for players to build with.

### Cited Findings
- BotW: interaction between objects ("multiplicative") replaced fixed solutions. A chemistry engine of elemental rules sits on top of physics — [Thumbsticks](https://www.thumbsticks.com/gdc-17-breaking-conventions-breath-of-the-wild)
- TotK: the director said community Ultrahand builds exceeded what the team imagined — [Zelda Universe](https://zeldauniverse.net/2024/06/05/tears-of-the-kingdom-director-and-producer-reflect-on-the-games-first-year/). Community record-length builds and a dedicated sharing site — [Zelda Universe](https://zeldauniverse.net/2024/04/02/tears-of-the-kingdom-creation-boasts-games-longest-object/); [Boss Rush](https://bossrush.net/2024/05/11/a-comprehensive-look-at-one-year-of-the-legend-of-zelda-tears-of-the-kingdom/)
- Minecraft: players build working computers and calculators from redstone. Cities and neural networks were "never scripted" by Mojang — [Metavert](https://metavert.io/emergent-gameplay); [Peachpit](https://peachpit.com/articles/article.aspx?p=2324462)
- Noita: the community documents spell interactions. A PC Gamer reviewer looked up community notes to understand a modifier — [PC Gamer](https://www.pcgamer.com/noita-review/). Hundreds of hours of secrets — [Bonus Stage](https://www.bonusstage.co.uk/tag/noita/)
- RimWorld: omitted features let players project stories ("story generator") — [GDC Vault](https://gdcvault.com/play/1024232/-RimWorld-Contrarian-Ridiculous-and)
- Dwarf Fortress: a world with persistent generated history, and stories that emerge from personality systems — [Technical.ly](https://technical.ly/brooklyn/2014/05/21/dwarf-fortress-adams/)
- Engagement spikes from new system content: Factorio CCU went from 34.7k (2020) to 118.7k (Space Age, Oct 2024) — [GamingOnLinux](https://gamingonlinux.com/2024/10/factorio-space-age-sold-over-400000-copies-and-sets-a-new-player-count-record). Satisfactory went from about 34.2k to 104.7k at 1.0 — [Game World Observer](https://gameworldobserver.com/2024/09/11/satisfactory-peaks-at-over-100k-ccu-launch). RimWorld set an all-time peak on 2025-07-20 — [SteamDB](https://steamdb.info/app/294100/charts/)
- Factorio players keep "opening new saves and play hundreds of hours after victory" — [GameGeeker](https://gamegeeker.com/games/factorio/review?country=US)

### Inferences
- Engagement compounds when player-built artefacts are (a) persistent, (b) reusable and parameterisable (blueprints, Autobuild, saves), and (c) shareable. This is the analogue of the planned "recipes". Sharing turns individual insight into community knowledge (wikis, build sites), which in turn makes deep rule sets easier to approach.
- Permanent world change is strongest in Dwarf Fortress (legends and history persist across forts) and Minecraft (persistent worlds). Roguelike Noita resets the world, and players return for knowledge rather than for a changed world. A game with a permanently changing world plus a reusable recipe system would combine both reasons to return.
- New rule sets added in expansions (planets, DLC mechanics) re-engage lapsed players more than numeric content does. This is inferred from the timing of CCU peaks; causation is not proven.

### Gaps
- No primary Wube statement on blueprint design intent was found (Friday Facts archive not reached).
- No quantitative data on share or download volume for blueprints, Workshop items, TotK builds or Powder Toy saves.
- Contents of Noita's GDC talk on wand design were not retrieved.
