# Player Motivation, Enjoyment, and Retention: Frameworks and Empirical Evidence (for classifying and measuring gameplay loops)

Research date: 2026-10-20. Design context: a 2D systemic natural-science sandbox with three pillars: (1) reward in proportion to effort, weighted toward insight over grind; (2) player actions permanently change the world, at small and huge scales; (3) players discover and codify actions as "recipes" by understanding the underlying rules.

**Method caveat for the report writer:** In this session, WebFetch and direct downloads were blocked. DNS failed for quanticfoundry.com, selfdeterminationtheory.org, northwestern.edu, medium.com and substack, and curl got a 403 from the proxy. Every finding below therefore comes from web-search result extracts of the cited pages, not from full-text reads. Some items are marked "[canonical, not re-verified this session]". These are well-established facts from the primary source at the URL given, but this session could not open that page. Check them before quoting exact wording.

---

## 1. MDA framework (Hunicke, LeBlanc & Zubek, 2004): the 8 aesthetics and how loops map to them

### Takeaway
MDA splits a game into Mechanics (rules and code), Dynamics (the run-time behaviour of mechanics acting on player input) and Aesthetics (the emotional responses the game evokes). Designers work from M to D to A, and players experience it from A to D to M. The eight aesthetics give a vocabulary for tagging which "kind of fun" each loop is meant to produce. The design's three pillars line up most closely with **Discovery**, **Challenge** and **Expression**, with Submission as a secondary aesthetic for the world-shaping pillar.

### Cited Findings
- MDA was published in 2004 (AAAI Workshop on Challenges in Game AI) by Robin Hunicke, Marc LeBlanc and Robert Zubek. It replaces the vague word "fun" with eight aesthetic categories. — [MDA paper PDF](https://users.cs.northwestern.edu/~hunicke/MDA.pdf); [Wikipedia: MDA framework](https://en.wikipedia.org/wiki/MDA_framework)
- The eight aesthetics, with the paper's taglines: **Sensation** (game as sense-pleasure); **Fantasy** (game as make-believe); **Narrative** (game as drama); **Challenge** (game as obstacle course); **Fellowship** (game as social framework); **Discovery** (game as uncharted territory); **Expression** (game as self-discovery); **Submission** (game as pastime). — [MDA paper (course mirror)](https://course.khoury.northeastern.edu/cs5150f14/readings/hunicke_mda.pdf); [Skeleton Code Machine, "The 8 kinds of fun"](https://www.skeletoncodemachine.com/p/the-8-kinds-of-fun)
- Designer and player perspectives: "from the designer's perspective, the mechanics give rise to dynamic system behavior, which in turn leads to particular aesthetic experiences". The player meets the aesthetics first. — [Yu-kai Chou, MDA analysis](https://yukaichou.com/gamification-analysis/mda-framework-hunicke-leblanc-zubek-mechanics-dynamics-aesthetics/)
- The paper's worked examples, which profile games as a mix of aesthetics [canonical, not re-verified this session]: Charades = Fellowship, Expression, Challenge; Quake = Challenge, Sensation, Competition, Fantasy; The Sims = Discovery, Fantasy, Expression, Narrative; Final Fantasy = Fantasy, Narrative, Expression, Discovery, Challenge, Submission. — [MDA paper PDF](https://users.cs.northwestern.edu/~hunicke/MDA.pdf)
- Researchers have tied MDA's Discovery directly to information-gap curiosity. Discovery "captures the desire for uncertainty and the pleasure of reducing information gaps through the exploratory actions a player takes in a game". — [DiGRA, "Integrating Curiosity and Uncertainty in Game Design"](https://dl.digra.org/index.php/dl/article/download/793/793/790)
- A common critique is that MDA names the target emotion but not its motivational cause, so it needs a motivation model such as SDT or Quantic Foundry alongside it. — [Game Developer, "MDA framework: unconnected connectivity"](https://www.gamedeveloper.com/design/mda-framework-unconnected-connectivity); [mechanicsofmagic.com](https://mechanicsofmagic.com/2022/12/20/blog-response-mda-8-kinds-of-fun-4/)

### Inferences
- **Mapping each loop to aesthetics.** For each loop, label the M (verbs and rules), the D (the emergent pattern, such as runaway reactions or ecosystem shifts) and the target A. Suggested mappings for the pillars:
  - "Recipe discovery": experiment, observe, form a hypothesis, codify. Primary aesthetic Discovery, secondary Challenge and Expression.
  - "Permanent world change": act, see a persistent consequence, reach a new state of the world. Primary aesthetic Expression, secondary Discovery and Submission.
  - "Insight-weighted reward": Challenge, but cognitive (puzzle-like) rather than dexterity-based.
- MDA itself has no measurement instrument. Pair it with PENS or the Quantic Foundry GMP for measurement (sections 2 and 4).

### Gaps
- The paper's verbatim text could not be fetched, so the four example game profiles above come from memory of the canonical paper and should be checked against the PDF.

---

## 2. Quantic Foundry Gamer Motivation Model (Nick Yee & Nicolas Ducheneaut)

### Takeaway
The model holds **12 motivations in 6 pairs**: Action (Destruction, Excitement), Social (Competition, Community), Mastery (Challenge, Strategy), Achievement (Completion, Power), Immersion (Fantasy, Story) and Creativity (Design, Discovery). It is built from factor analysis of over a million self-selected survey respondents. The findings most relevant to this design:
- Age explains more variance than gender.
- Competition declines most with age, and Strategy is the most age-stable motivation.
- Interest in Strategy has fallen most among all 12 motivations since 2015.
- The Creativity cluster (Design, Discovery) is the natural target audience for a discovery sandbox.

### Cited Findings
- **The 12 motivations** are Destruction, Excitement, Competition, Community, Challenge, Strategy, Completion, Power, Fantasy, Story, Design and Discovery. — [Quantic Foundry home](https://quanticfoundry.com/); [Handy reference chart](https://quanticfoundry.com/2015/12/15/handy-reference/)
- **The 6 clusters (pairs)** are Action = Destruction + Excitement; Social = Competition + Community; Mastery = Challenge + Strategy; Achievement = Completion + Power; Immersion = Fantasy + Story; Creativity = Design + Discovery. A PMC review confirms that Design and Discovery form the Creativity cluster and that Completion pairs with Power. — [Handy reference chart](https://quanticfoundry.com/2015/12/15/handy-reference/); [PMC review, PMC9872527](https://pmc.ncbi.nlm.nih.gov/articles/PMC9872527)
- At a higher level, the clusters group into three bridges [canonical, not re-verified this session]: Action-Social, Mastery-Achievement and Immersion-Creativity. Discovery also loads near Strategy. — [Gamer Motivation Model Overview PDF (2015)](https://quanticfoundry.com/wp-content/uploads/2015/12/Gamer-Motivation-Model-Overview.pdf)
- **Definitions from the reference sheets:**
  - Discovery: "explore the world… tinker, experiment".
  - Design: expression and customization.
  - Completion: finish everything the game has to offer.
  - Strategy: "the enjoyment of gameplay that requires careful decision-making and planning".
  - Sources: [GMM Reference Sheets v3 (uploaded 2026-09)](https://quanticfoundry.com/wp-content/uploads/2026/09/Gamer-Motivation-Model-Reference-v3.pdf); [GMM Reference (2019)](https://quanticfoundry.com/wp-content/uploads/2019/04/Gamer-Motivation-Model-Reference.pdf); [2016 gamer-generation post](https://quanticfoundry.com/2016/02/10/gamer-generation/)
- **A v3 model** was published in a reference sheet dated September 2026. The search extract did not show its structural changes against v2. — [GMM Reference v3 PDF](https://quanticfoundry.com/wp-content/uploads/2026/09/Gamer-Motivation-Model-Reference-v3.pdf)
- **Sample sizes over time:**
  - About 140,000 gamers in the early-2016 age analysis. — [2016-02-10 post](https://quanticfoundry.com/2016/02/10/gamer-generation/)
  - Over 239,000 gamers in the August 2016 competition analysis. — [2016-08-11 post](https://quanticfoundry.com/2016/08/11/appeal-of-competition/)
  - About 250,000 respondents in a 2016 secondary summary. — [gamerboom.com](https://gamerboom.com/archives/92651)
  - About 1.57 million gamers surveyed between June 2015 and April 2024. Secondary coverage cites 1.5 to 1.7 million and says China is excluded. — [Quantic Foundry 2024-05-21 strategy-decline post](https://quanticfoundry.com/2024/05/21/strategy-decline/); [Gigazine coverage (2024-06-02)](https://gigazine.net/gsc_news/en/20240602-game-strategy-thinking-planning-decline/)
  - The current site claims "over 2 million players across 4,000+ titles" (as of 2026). — [Quantic Foundry home](https://quanticfoundry.com/)
- **Sample composition** (2026 Evolution of Play report): 74% male, 21% female, 5% non-binary. Respondents are self-selected and unpaid. — [Evolution of Play Report](https://quanticfoundry.com/evolution-of-play/); [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9872527)
- **Gender (2015):**
  - The top primary motivations for men are Competition and Destruction. For women they are Completion and Fantasy.
  - Gender differences "align with stereotypes, but [are] small compared to age". Older gamers are "genuinely less motivated by… highly competitive or adrenaline-filled games".
  - Source: [Quantic Foundry 2015-08-28 gender post](https://quanticfoundry.com/2015/08/28/gender-differences-in-gaming/)
- **Age (2016):**
  - Competition changes the most with age, at r = .28 with age. Age explains roughly 3x the variance in Competition that gender does.
  - The decline in Competition is faster for men than for women.
  - Strategy is the most age-stable motivation: r = −.05 in 2016, and r = .06 (r² = .004) in 2024.
  - Discovery has a weak age correlation, about r = −.06.
  - Sources: [2016-02-10 gamer-generation post](https://quanticfoundry.com/2016/02/10/gamer-generation/); [2016-08-11 competition post](https://quanticfoundry.com/2016/08/11/appeal-of-competition/); [2024-05-21 strategy post](https://quanticfoundry.com/2024/05/21/strategy-decline/)
- A secondary summary of the roughly 250k sample says the leading motivation for ages 13–25 is competition ("contest"), while for ages 36+ it is Fantasy, Completion and Destruction. This is a secondary source and gives no percentages. — [gamerboom.com](https://gamerboom.com/archives/92651)
- **Strategy decline (published 2024-05-21):**
  - Strategy showed the largest decline of the 12 motivations, across genders and nationalities.
  - If the 2015 average is set to the 50th percentile, the average 2024 gamer sits around the 33rd percentile. Put another way, 67% of 2024 gamers value strategy and planning less than the average 2015 gamer did.
  - The cause is unknown. The authors floated attention spans as a possible explanation, but the finding is correlational.
  - Sources: [Quantic Foundry strategy-decline](https://quanticfoundry.com/2024/05/21/strategy-decline/); [Gigazine](https://gigazine.net/gsc_news/en/20240602-game-strategy-thinking-planning-decline/); [Push Square](https://www.pushsquare.com/news/2024/05/bombshell-report-finds-players-becoming-less-interested-in-deep-strategy-games)
- In a 2025 interview, Yee repeated the figure ("the average gamer in 2025 would only be at the 33rd percentile"). He suggested that hybrids such as *Balatro* combine strategy with surprise and novelty. — [Player Driven interview, Part 1](https://playerdriven.substack.com/p/quantic-foundrys-nick-yee-on-gamer)
- **Gamer types and segments:** Quantic Foundry publishes 9 "Quantic Gamer Types" and a GDC 2020 player-segment deck. One segment there is "most interested in Design (customization, expression)". — [9 Gamer Types](https://quanticfoundry.com/gamer-types/); [GDC 2020 slides](https://quanticfoundry.com/wp-content/uploads/2020/08/GDC-2020-Slides-Player-Segments-Quantic-Foundry.pdf)
- **Genre and title data** sit in paid products. The Motivation Insight Report (2025 edition, listed at $2,950) charts all 12 motivations by gender and age. A sample Minecraft audience report also exists. — [Motivation Insight Report](https://quanticfoundry.com/insight-report/); [Example Audience Report: Minecraft](https://quanticfoundry.com/wp-content/uploads/2017/05/Example-Audience-Report-Minecraft.pdf); [Audience Profiles](https://quanticfoundry.com/audience-profiles/)
- The model is proprietary and "not openly accessible to the scientific community due to copyright protection". — [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9872527)

### Inferences
- The pillars map onto the GMP as follows: Pillar 3 (recipes) maps to **Discovery** plus **Strategy**; Pillar 2 (world change) maps to **Design** and **Destruction** (large-scale changes); Pillar 1 (insight over grind) means leaning toward Strategy and Challenge and away from Completion and Power grind.
- Because Strategy is the most age-stable motivation, an insight-driven audience should be durable across ages, even though the population mean has fallen.
- The 2024 decline in Strategy suggests making deduction feel rewarding through surprise and spectacle, as in Yee's *Balatro* point. Reward insight with visible, satisfying world change, not just a quiet unlock.
- A practical measurement step is to run the free Gamer Motivation Profile on playtesters, then segment playtest metrics by each tester's Creativity and Mastery scores.

### Gaps
- **Genre-level scores** (which genres score highest on Discovery, Design, Strategy, Completion and Power) were not reachable. They sit in paid reports and in blog posts that could not be fetched. Do not claim specific genre rankings without checking them.
- **Age correlations for Completion, Power, Discovery and Design** beyond the figures above were not retrieved.
- The **v3 model changes** (September 2026) are unknown.

---

## 3. Bartle player types, critiques, and successors (Yee's components of online play)

### Takeaway
Bartle's 1996 four types (Achievers, Explorers, Socializers, Killers) come from a single designer's observation of MUD players. Yee's factor-analytic work (about 3,000 MMO players) replaced them with **3 components and 10 subcomponents**. Two findings matter here: Explorer splits into "mapping the world" versus "understanding mechanics", and achievement correlates with competition. Later confirmatory work found 7 factors.

### Cited Findings
- **Bartle (1996)**, "Hearts, Clubs, Diamonds, Spades: Players Who Suit MUDs", defines the four types on two axes: acting on versus interacting with, and players versus world [canonical, not re-verified this session]. — [Bartle 1996](https://mud.co.uk/richard/hcds.htm)
- **Yee (2006)** factor-analysed about 3,000 MMORPG players. He found 10 motivation subcomponents grouped into 3 overarching components: **Achievement**, **Social** and **Immersion**. — [Yee 2006 PDF mirror](https://eclass.uniwa.gr/modules/document/file.php/EEE195/2023-2024/Online%20gaming%20addiction/yee%202006.pdf); [SFU Summit](https://summit.sfu.ca/item/212)
- The 10 subcomponents [canonical, not re-verified this session]:
  - Achievement: Advancement, Mechanics, Competition.
  - Social: Socializing, Relationship, Teamwork.
  - Immersion: Discovery, Role-Playing, Customization, Escapism.
  - Source: [Yee 2006 PDF](https://eclass.uniwa.gr/modules/document/file.php/EEE195/2023-2024/Online%20gaming%20addiction/yee%202006.pdf)
- **Where the data contradicts Bartle:**
  - Socializing and role-playing are independent motivations.
  - Achievement and competition correlate at r = .41, against Bartle's separation of Achievers and Killers.
  - Explorer splits into two motivations: one about mapping and exploring the world, the other about understanding game mechanics.
  - Bartle's Explorer type was not validated as a single construct.
  - Sources: [Yee, "Revisiting Bartle's Types"](https://nickyee.com/facets/revisiting.html); [Daedalus archive](https://nickyee.com/daedalus/archives/001298.php?page=9)
- **Yee's reply to Bartle:** "Brainstorming motivations is as subjective as brainstorming player types". The difference is that motivations are then empirically tested. — [Daedalus archive](https://nickyee.com/daedalus/archives/001298.php?page=8)
- **Methodological successor:** Kahn et al.'s 2011 work on 3,818 online gamers applied combined exploratory and confirmatory factor analysis. It found 7 motivational factors, not Yee's 10 PCA components. — [Springer, Behavior Research Methods (2011)](https://www.springermedizin.de/article/10.3758/s13428-011-0091-y)
- Quantic Foundry's GMP (section 2) is the commercial descendant of Yee's work, and Yee co-founded the company. — [Wikipedia: Nick Yee](https://en.wikipedia.org/wiki/Nick_Yee)

### Inferences
- Yee's split of "Explorer" into world-mapping and mechanics-understanding matters directly for Pillar 3. The recipe system serves the **mechanics-understanding** explorer. Wide-open terrain serves the **mapping** explorer. Treat these as two separate loops with separate metrics, such as recipes codified per hour versus area revealed.
- Avoid using Bartle types for segmentation. They are not empirically validated.

### Gaps
- The exact factor loadings and sample N from Yee (2006) were not retrieved. "About 3,000" is from the search extract.

---

## 4. Self-determination theory in games (Ryan, Rigby & Przybylski; PENS)

### Takeaway
The PENS (Player Experience of Need Satisfaction) model holds that games are motivating because they satisfy needs for **competence, autonomy and relatedness**. Across four studies (2006), in-game autonomy and competence predicted enjoyment, preference for future play and short-term changes in well-being. Intuitive controls and presence were linked to need satisfaction.

### Cited Findings
- **Ryan, Rigby & Przybylski (2006)**, "The Motivational Pull of Video Games: A Self-Determination Theory Approach", *Motivation and Emotion* 30:347–363. DOI 10.1007/s11031-006-9051-8. — [Rochester-hosted PDF](https://www.rochester.edu/warner/lida/wp-content/uploads/2022/11/02bfe513dd59366750000000.pdf); [SDT-hosted PDF](https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf)
  - Note on page numbers: some citations give pp. 344–360, but the DOI and repository records give 347–363. — [ACU research bank](https://acuresearchbank.acu.edu.au/item/8q128/the-motivational-pull-of-video-games-a-self-determination-theory-approach)
- **Design of the studies:** Studies 1–3 had participants play 1, 2 and 4 games respectively. Perceived in-game autonomy and competence were "associated with game enjoyment, preferences, and changes in well-being pre- to post-play". Competence and autonomy were also related to "the intuitive nature of game controls, and the sense of presence or immersion". — [Rochester PDF](https://www.rochester.edu/warner/lida/wp-content/uploads/2022/11/02bfe513dd59366750000000.pdf)
- **Study 4** surveyed an online community of multiplayer gamers. Autonomy, competence and relatedness "independently predict enjoyment and future game play". — [Rochester PDF](https://www.rochester.edu/warner/lida/wp-content/uploads/2022/11/02bfe513dd59366750000000.pdf); [ScienceDaily press release (2006-12)](https://www.sciencedaily.com/releases/2006/12/061226134706.htm)
- **PENS subscales:** in-game competence, in-game autonomy, relatedness, presence/immersion and intuitive controls. Outcomes measured include enjoyment and preference for future play. — [SDT: PENS page](https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/)
- **Przybylski, Rigby & Ryan (2010)**, "A Motivational Model of Video Game Engagement", *Review of General Psychology* 14(2):154–166, doi 10.1037/a0019440. It argues that both the appeal of games and their effects on well-being rest on satisfying competence, autonomy and relatedness. — [SDT PDF](https://selfdeterminationtheory.org/SDT/documents/2010_PrzybylskiRigbyRyan_ROGP.pdf); [Essex repository](https://repository.essex.ac.uk/7228/)
- A secondary summary of the 2010 review says a highly rated game (*Zelda: Ocarina of Time*) raised experienced autonomy and competence more than a poorly rated game did. This is a blog summary, so treat it with caution. — [vgresearcher blog](https://vgresearcher.wordpress.com/2010/07/31/a-motivational-model-of-the-gamerface-przybylski-et-al-2010/)
- **Przybylski, Ryan & Rigby (2009)**, "The Motivating Role of Violence in Video Games" (*PSPB*), found that enjoyment and future play are driven by competence and autonomy, not by violent content as such [summary of abstract; specific statistics not retrieved]. — [SDT PDF](https://selfdeterminationtheory.org/SDT/documents/2009_PrzbylskiRyanRigby_PSPB.pdf)
- A later study (QUT eprint) reports that all three SDT needs were associated with more time spent playing. — [QUT eprint](https://eprints.qut.edu.au/222407/1/105951.pdf)
- **Critiques:** the samples were biased and the range of genres tested was limited. — [Scribd summary](https://www.scribd.com/document/210196521/Research-Writing) (weak source)

### Inferences
- Mapping to the pillars:
  - Pillar 1 (insight) maps to **competence**.
  - Pillar 3 (player-authored recipes) maps strongly to **autonomy** (choice) and competence (mastery of rules).
  - Pillar 2 (persistent consequences) maps to autonomy, because meaningful choice requires effects that last.
  - Relatedness is unaddressed unless recipes can be shared.
- Measurement: give a short PENS-style questionnaire after each playtest session, and track the competence and autonomy subscale means for each loop or build.

### Gaps
- Exact correlation and regression coefficients and per-study Ns from the 2006 and 2010 papers could not be extracted, because the PDFs were unreachable. The writer should not quote numeric effect sizes from this section.

---

## 5. Reward schedules, compulsion versus engagement loops, grind, fairness, and effort justification

### Takeaway
Variable-ratio rewards produce persistent responding. The strongest monetized form, the loot box, has a replicated but small association with problem gambling (η² ≈ .05). The IKEA effect shows that effort raises the value people place on an outcome **only when the task is successfully completed**. That supports "effort leads to reward" but not open-ended grind. No direct, peer-reviewed measure of grind's effect on satisfaction was found.

### Cited Findings
- **Zendle & Cairns (2018)**, PLoS ONE, 2018-11-21, n = 7,422: loot box spending is linked to problem gambling severity. The authors note the causal direction is unclear: loot boxes may be a gateway, or problem gamblers may be drawn to them. A 2019 correction removed a preprint statistic claiming 37.7% of variance explained. — [PLoS ONE 2018](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0206767); [Correction](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0214167)
- **Replication (2019)**, PLoS ONE 14(3): e0213194. Mean monthly loot box spend was $11.14 for non-problem gamblers, $21.87 for low-risk, $27.55 for moderate-risk and $38.24 for problem gamblers. Effect size η² = 0.051, compared with 0.054 originally. — [PLoS ONE replication](https://journals.plos.org/plosone/article/file?id=10.1371%2Fjournal.pone.0213194&type=printable)
- **Zendle, Cairns, Barnett & McCall (2020)**, *Computers in Human Behavior*: paying for loot boxes is linked to problem gambling "regardless of specific features such as cash-out and pay-to-win". — [York Research Database](https://pure.york.ac.uk/portal/en/publications/paying-for-loot-boxes-is-linked-to-problem-gambling-regardless-of/)
- Zendle (2020, *Addiction*) measured how common loot boxes are in mobile and desktop games. — [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/add.14973)
- **IKEA effect (Norton, Mochon & Ariely, 2012, *Journal of Consumer Psychology*):**
  - Labor increases valuation, but "successful completion is an essential component". People who built and then destroyed their creations, or who failed to complete them, showed no boost.
  - The effect holds for both do-it-yourselfers and novices.
  - It is linked to effort justification (the classic initiation experiments).
  - Sources: [Harvard DASH PDF](https://dash.harvard.edu/bitstreams/7312037d-2473-6bd4-e053-0100007fdf3b/download); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1057740811000829)
- Claims that grind raises perceived value "via the IKEA effect" appear only in non-peer-reviewed design blogs. — [Medium/Bootcamp, "role of grinding"](https://medium.com/design-bootcamp/product-design-and-psychology-the-role-of-grinding-in-video-game-design-72a2c70a9ae4)

### Inferences
- **Compulsion loop versus engagement loop.** This is a working distinction for the design team, not a sourced definition: a compulsion loop rewards repetition on an unpredictable schedule, regardless of what the player understands. An engagement or mastery loop gives rewards that scale with competence and understanding.
- Pillar 1 maps onto the IKEA finding: effort pays off in value only when it ends in a **completed, owned** result. Here that is a codified recipe or a persistent change to the world. Recipes as authored artifacts that the player "built" are a strong use of the IKEA effect.
- Variable outcomes can still be used ethically. Natural systems produce variable results, and surprise is a feature that fits Yee's *Balatro* point. Keep the variability **informational** (it teaches the rules) rather than purely monetary or random.

### Gaps
- No peer-reviewed quantitative study was found linking grind or time-gated progression to satisfaction or churn.
- No study on players' perceived fairness of reward relative to effort was retrieved.
- Hamari et al. (2017) on in-game purchases was not retrieved.
- No authoritative source defining "compulsion loop" was retrieved (the Game Developer article was not found).

---

## 6. Curiosity and discovery (information-gap theory; exploration motivation)

### Takeaway
Loewenstein (1994) defines curiosity as a drive to close an **information gap**: a noticed gap between what one knows and what one wants to know. Game researchers explicitly use this theory to explain MDA's Discovery aesthetic. Empirical surveys find that exploration, simulation and collection games are the ones players most often name as curiosity-inducing.

### Cited Findings
- A 2024 framework paper in the *International Journal of Human–Computer Interaction* grounds game curiosity in Loewenstein's (1994) theory and studies it with a player-perspective questionnaire. — [Taylor & Francis, "Exploring Curiosity in Games: A Framework and Questionnaire Study of Player Perspectives" (2024)](https://www.tandfonline.com/doi/full/10.1080/10447318.2024.2325171)
- Loewenstein also framed curiosity as a preference for uncertainty that arises from an information gap. Discovery in MDA is "the pleasure of reducing information gaps through the exploratory actions a player takes". — [DiGRA paper](https://dl.digra.org/index.php/dl/article/download/793/793/790)
- In a survey by Gómez-Maureira & Kniestedt, games involving **exploration, social simulation and collecting** ranked highly as curiosity-inducing. — [ResearchGate, "Games that Make Curious"](https://www.researchgate.net/publication/327215825_Games_that_Make_Curious_An_Exploratory_Survey_into_Digital_Games_that_Invoke_Curiosity); [Leiden repository](https://scholarlypublications.universiteitleiden.nl/access/item:3217499/view)
- A JCU study reports that different dimensions of curiosity differentially predict video game preferences and play. — [JCU ResearchOnline PDF](https://researchonline.jcu.edu.au/83317/7/83317.pdf)
- Incomplete information (truncated video ads) triggers a curiosity drive and the urge to seek more information (2024, advertising context). — [PMC11378734](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11378734/)

### Inferences
- For Pillar 3, information-gap theory suggests making gaps **visible and bounded**, for example a partially revealed recipe book, observed but unexplained phenomena, or "?" entries. A gap only motivates once the player notices it and believes it can be closed.
- Measurable proxies for curiosity loops include:
  - time from first observing a phenomenon to codifying the recipe for it;
  - the share of known gaps the player deliberately attempts;
  - the experiment-to-hypothesis ratio.

### Gaps
- The Loewenstein 1994 original (*Psychological Bulletin*) was not directly retrieved.
- Learning-progress accounts of curiosity (Gottlieb, Oudeyer) were not retrieved.
- No game-telemetry study linking curiosity mechanics to retention was found.

---

## 7. Retention metrics: D1, D7 and D30 industry benchmarks

### Takeaway
GameAnalytics' 2025 mobile benchmarks put median D1 at about 22% (top 10% about 40%), median D7 just under 4% (top 10% about 11–12%), and median D28/D30 under 1% (top 10% about 4%). Retention declined from 2024 to 2025. Openly available genre-level tables are mostly stale (AppsFlyer, Q3 2022) or come from unreliable aggregators.

### Cited Findings
- **GameAnalytics Mobile Benchmarks 2025** (about 11,600 apps; summarized in 2025):
  - D1 median (P50) about 22%, top 10% (P90) about 40%.
  - D7 P50 just under 4%, P90 about 11–12% for most of 2025.
  - D30 median about 0.7%, top 10% about 4%.
  - GameAnalytics reports long-term retention as **D28**, and "75% of games fail to exceed 3%" D28.
  - D1 "continued its downward trend from 2024".
  - Sources: [GameDevReports summary of GameAnalytics 2025](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks); [Game Industry Library: GA 2025](https://gameindustrylibrary.com/documents/gameanalytics-mobile-gaming-benchmarks-2025)
- **GameAnalytics Mobile and PC Benchmarks 2026** (published January 2026; 16,262 titles with at least 1,000 MAU). This is the first edition to include PC. — [GameDevReports summary (2026)](https://gamedevreports.substack.com/p/gameanalytics-mobile-and-pc-game); [InvestGame PDF (2026-01-27)](https://investgame.net/wp-content/uploads/2026/01/2026-01-27-2026-mobile-pc-benchmarks_compressed.pdf); [InvestGame mobile retention benchmarks 2026 PDF (2026-01-20)](https://investgame.net/wp-content/uploads/2026/01/2026-01-20-Mobile_retention_benchmarks_2026.pdf)
  - The 2026 figures, including the PC numbers, were not extracted. One sponsored summary reports a top-1% D1 of 64–68%, which looks inconsistent with the other data and should be treated as unverified.
- **Genre-level D30 tables:**
  - Widely circulated figures (Match about 7.15%, Puzzle about 5.35%, RPG about 3.48%, Simulation about 2.96%, Hyper-casual about 1.38%) trace back to **AppsFlyer Q3 2022**. Aggregators state that openly published 2025/26 genre-level data does not exist.
  - Other aggregators give Mid-core about 6.8%, Casual about 3.6% and Hyper-casual about 2.1% at D30, citing Adjust, AppsFlyer and Sensor Tower.
  - All of these are low-reliability marketing pages that cite each other.
  - Sources: [Segwise (2026)](https://segwise.ai/blog/mobile-gaming-app-user-retention-strategies); [UXCam (2026)](https://uxcam.com/blog/mobile-app-retention-benchmarks/); [AppsFlyer State of Gaming App Marketing 2024](https://www.appsflyer.com/resources/reports/gaming-app-marketing-2024-report/)
- AppAgent publishes higher tiers for commercially marketed (UA-funded) games, so the choice of benchmark matters. — [AppAgent](https://appagent.com/?p=61637)

### Inferences
- These are mobile free-to-play benchmarks. A premium 2D PC sandbox should benchmark against the GA 2026 PC section and track session-based measures alongside D-retention, such as days played in the first 14 days, median session length and return after a content update.
- Proposed loop-level retention diagnostics (an inference, not sourced):
  - D1 tests whether the first discovery loop pays off in the first session (time to first recipe).
  - D7 tests whether the player has formed a self-directed goal (an autonomy signal).
  - D30 tests whether world change has compounded into a sense of ownership (IKEA effect).

### Gaps
- No peer-reviewed or vendor study was retrieved that ties specific loop features to D1, D7 or D30. The figures for PC and premium titles are not extracted.

---

## 8. Flow theory in games (Csikszentmihalyi; Chen; GameFlow)

### Takeaway
Flow is the state of deep absorption that occurs when challenge matches skill and the activity has clear goals and immediate feedback. Jenova Chen's 2006 MFA thesis and the game *flOw* operationalized flow through **player-driven, implicit dynamic difficulty**: players choose how hard to play through in-game choices, rather than the system adjusting difficulty passively.

### Cited Findings
- Chen's USC MFA thesis, "Flow in Games", builds on Csikszentmihalyi's flow theory. It gives players "subconscious choices" so they can actively customize their own optimal experience. It contrasts this active approach with passive DDA, which relies on "analyzing incomplete in-game data". — [Chen thesis PDF](https://www.jenovachen.com/flowingames/Flow_in_games_final.pdf); [Abstract](https://www.jenovachen.com/flowingames/abstract.htm)
- In *flOw*, players set the difficulty by choosing which organisms to eat and which to avoid, and by choosing when to descend. The game had 100,000 downloads in its first two weeks and over 650,000 by July (2006 web version). — [Wikipedia: Flow (video game)](https://en.wikipedia.org/wiki/Flow_(video_game)); [Engadget, 2006-09-12](https://www.engadget.com/2006-09-12-flow-in-games-an-interactive-thesis-on-dynamic-difficulty.html)
- **GameFlow** (Sweetser & Wyeth, 2005, *Computers in Entertainment*) adapts flow into 8 evaluation criteria [canonical, not re-verified this session]: concentration, challenge, player skills, control, clear goals, feedback, immersion and social interaction. — [Wikipedia: Jenova Chen (context)](https://en.wikipedia.org/wiki/Jenova_Chen) (no direct GameFlow source was retrieved; see Gaps)
- A custom game study used DDA to increase player enjoyment. — [arXiv 1806.04471](https://arxiv.org/pdf/1806.04471)

### Inferences
- In a sandbox, Chen's model of player-chosen difficulty fits better than system-imposed DDA. The player picks which unknown phenomenon to investigate, which acts as a self-selected difficulty level.
- To support flow, scientific "puzzles" need clear local goals (an open question) and immediate, legible feedback (a visible reaction).

### Gaps
- The Sweetser & Wyeth (2005) GameFlow paper was not retrieved this session. Its 8 elements are listed from canonical knowledge.
- Csikszentmihalyi's primary texts were not retrieved.
- No quantitative study linking flow scores to retention was retrieved.
