# Research Task: Gameplay Loops of Popular Games

Status: **first pass complete (2026-10-20)** — see [02-gameplay-loops-findings.md](02-gameplay-loops-findings.md). Review-text mining is the remaining step. (Decision D6 in [../design/01-pillars.md](../design/01-pillars.md#0-decision-log).)

## Goal

Measure, group and analyse what players enjoy and dislike in the gameplay loops of popular games, and what keeps them coming back, so that our core-loop decisions rest on evidence rather than intuition.

## Questions to answer

1. What loop structures do successful games use (moment-to-moment, session, and long-term meta loops), and how do they nest?
2. Which loop features correlate with **retention** (players returning after 1 day, 7 days, 30 days, and long-term play time)?
3. Which features players **praise or complain about** most, grouped by category, such as grind, discovery, mastery, expression, social and progression?
4. How do **systemic / sandbox** games (our genre) differ from authored, content-driven games on the measures above?
5. Specifically for our pillars: how do players respond to (a) reward-per-effort fairness, (b) permanent world change, and (c) rule discovery?

## Method

1. **Select the games.** About 30–50 titles across three groups:
   - Systemic and sandbox games: Noita, Minecraft, Terraria, Dwarf Fortress, Teardown, Breath of the Wild / Tears of the Kingdom, Factorio, Oxygen Not Included.
   - Knowledge-progression games: Outer Wilds, Baba Is You, Return of the Obra Dinn.
   - Broad commercial hits as a control group, across genres.
2. **Break each game's loop down** into a common schema: core action → immediate feedback → resource/reward → spend or invest → new capability → back to the core action. Record the time scale and the effort type (time, skill, insight, risk) at each step.
3. **Gather quantitative signals:**
   - Player counts and how long players stay (public trackers).
   - Review sentiment: sample Steam reviews per title through the public review API and tag them by theme. Topic modelling or LLM-assisted coding is an option, validated by spot-checking samples by hand.
4. **Map findings to frameworks** so results are comparable: MDA (Mechanics–Dynamics–Aesthetics), Quantic Foundry's gamer motivation model, Bartle player types, and self-determination theory (competence, autonomy, relatedness).
5. **Synthesise:** a table of loop features × enjoyment/retention signals, and a short list of findings that apply directly to our design, each tied to a pillar.

## Deliverables

- `docs/research/02-gameplay-loops-findings.md`: the findings report with a full list of sources.
- A dataset (CSV) of games × loop features × signals, so the analysis can be redone and extended.
- A list of recommended changes to the design docs, where the evidence calls for them.

## Caveats to watch

- Review data is self-selected: players who leave reviews aren't representative of all players.
- Player counts reflect marketing and price as well as loop quality.
- Correlation is not causation. Treat the findings as hypotheses to test in our prototype, not as facts.

## Starting sources

- MDA framework (Hunicke, LeBlanc, Zubek) — https://users.cs.northwestern.edu/~hunicke/MDA.pdf
- Quantic Foundry gamer motivation model — https://quanticfoundry.com/gamer-motivation-model/
- Bartle taxonomy of player types — https://en.wikipedia.org/wiki/Bartle_taxonomy_of_player_types
- Self-determination theory — https://en.wikipedia.org/wiki/Self-determination_theory
- Steam user reviews API (getreviews) — https://partner.steamgames.com/doc/store/getreviews
- SteamDB (player count history) — https://steamdb.info/
- Game design / core loop overview — https://en.wikipedia.org/wiki/Game_design
