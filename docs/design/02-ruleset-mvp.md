# MVP Ruleset — 2D Natural Science

Status: second draft (2026-10-20). It follows decisions D1–D14 and the research-backed design rules R1–R16 in [01-pillars.md](01-pillars.md#2a-design-rules-from-player-research). Rule numbers in brackets, e.g. [R4], show where each rule applies.

The MVP has one job: show that **finding out how simple natural rules interact, and turning that into recipes, is fun**. Anything that doesn't serve that is a placeholder.

## 1. The world model

- **A 2D grid of cells**, side-on view, in the style of falling-sand games. Each cell holds one material plus a few state values.
- **Per-cell state:** `material`, `temperature`, `moisture` (optional for the MVP), and `age` (used for growth and decay).
- **Simulation tick:** each cell updates based on its own state and its 8 neighbours. Every rule is local; large-scale effects come from local rules adding up. That is Pillar 2's "one set of rules at every scale".
- **No special cases [R11].** Each material behaves only according to its property values. A rule that would apply "except here" is a bug.
  - Structural support needs particular care. Rigid solids hold up only what a declared support rule says they can. Players notice when a structure "should collapse but doesn't".
- **Performance budget [R15].** The prototype must hold 60 fps for the full world on a mid-range laptop. A drop in frame rate is a gameplay bug, not polish.

## 2. The primitives

This is the smallest set I think still produces interesting combinations. Every material is just a set of values for these properties.

| # | Primitive | What it controls | Example behaviour |
|---|---|---|---|
| P1 | **Phase** (rigid solid, powder, liquid, gas) | How a cell moves | Sand piles up, water spreads, steam rises |
| P2 | **Density** | Which material sinks and which floats | Wood floats on water; stone sinks |
| P3 | **Gravity** | A constant downward bias on movement | Unsupported powder falls; gas rises against it |
| P4 | **Heat** (temperature, heat capacity, conductivity) | How energy is stored and spreads | Metal conducts heat; stone holds heat for a long time |
| P5 | **Phase thresholds** (melting and boiling points) | When heat changes a material's phase | Ice → water → steam; sand → glass |
| P6 | **Reactions** (A + B + condition → C + D ± energy) | Chemistry, combustion, erosion | Wood + heat → fire → ash + heat |
| P7 | **Growth** (living cells spread when conditions are met) | Biology and regrowth | A seed with water, light and soil becomes a plant |
| P8 | **Energy inputs** (sunlight, deep geothermal heat) | Where new energy comes from | The sun warms the surface; the deep earth is hot |
| P9 | **Humidity** (water vapour in air; saturation rises steeply with temperature) | Evaporation, clouds, rain, plant water use | Moist air rising up a mountain cools, clouds form, and it rains; the far side stays dry |
| P10 | **Wind** (a prevailing air flow, deflected upward by terrain) | Where moisture goes | Ocean air brings rain to the windward slope and leaves a rain shadow behind |

P9 and P10 were added in prototype v0.3 (2026-10-20), after playtest 01 asked how mountains, forests and deserts shape the climate. Water is conserved through the whole cycle: ocean inflow, evaporation, plants releasing vapour, cloud, rain, soaking into soil, and drying out. Raindrops can be partial cells, and they merge when they touch.

**Conservation (from section 4 of the pillars doc):** heat energy is conserved inside the simulation. It enters only through P8 and leaves only through slow radiation into the sky. Every reaction in P6 declares its energy change explicitly. This is the main balance lever (D3).

Deliberately left out of the MVP: electricity, pressure, magnetism and light as a simulated quantity (wind was added in v0.3). Each is a candidate expansion once the core is shown to work. Adding new primitives is also the planned long-term way to bring players back, instead of content packs [R16].

**Randomness in the simulation is noise the player can learn from [R7].** Small random variations, such as which neighbour a powder falls towards, keep the world from looking mechanical. But the *outcome* of a reaction is decided by its conditions, never by a dice roll. Run the same arrangement under the same conditions and you get the same result.

## 3. Starter materials (about 15)

| Material | Phase | Notes |
|---|---|---|
| Air | gas | The empty or default cell |
| Stone | rigid solid | Hard to dig; holds heat |
| Sand | powder | Melts into glass at high temperature |
| Dirt | powder | Grows plants; turns to mud when wet |
| Mud | powder (slow) | Dries back to dirt; fires into brick |
| Clay | rigid solid | Fires into brick |
| Water | liquid | Freezes into ice; boils into steam; erodes dirt slowly |
| Ice | rigid solid | |
| Steam | gas | Condenses back into water when it cools |
| Wood | rigid solid | Burns; floats |
| Plant / seed | rigid solid, living | Grows; dies into wood or organic matter |
| Fire | gas, short-lived | A reaction state; produces heat and ash |
| Ash | powder | Fertilises soil (speeds growth) |
| Lava | liquid | Very hot; cools into stone |
| Ore → Metal | rigid solid | Ore plus heat and charcoal gives metal (early metallurgy) |
| Glass, Brick | rigid solid | Crafted materials that only come from reactions |

## 4. Player verbs and recipes

### Verbs (MVP)

The player is a small character in the grid with five verbs:

1. **Dig / collect.** Take a cell into the inventory. Effort scales with how hard the material is.
2. **Place.** Put a material from the inventory into a cell.
3. **Ignite / heat.** Needs a heat source the player has already obtained (to start with, there's no free fire).
4. **Pour / scatter.** Place liquids and powders in a stream.
5. **Observe.** Inspect a cell to see its material and, once the relevant knowledge is unlocked, its temperature and other properties. Knowledge improves the instruments.

**Unlocks widen capability, not stats [R6].** What the player unlocks is new instruments (thermometer, scale, sample burner), more precision for them, and new verbs. There are no damage or speed multipliers.

**Experiments are cheap [R3].** Small tests should cost little, be quick to set up, and be easy to contain, for example in a small test crucible or a sandbox corner. Energy cost and risk apply to large-scale use, not to finding things out.

### Onboarding [R1]

- **The starting area is a set of puzzles waiting to be noticed.** It contains two or three visible phenomena that aren't explained, for example:
  - steam rising from a warm spring
  - ice forming on stone in the shade
  - a fire that has spread along a line of dry grass
- **The first observations happen in the first minutes.** Each of these phenomena appears in the journal as a "?" entry within the first few minutes of play.
- **No text tutorial beyond controls.** The first reactions the player sees *are* the tutorial.
- **Target:** the first reaction is observed within 5 minutes, and the first recipe is saved within the first hour. Both are measured in the prototype.

### Recipes

There are two different things here, and keeping them apart matters:

- **A reaction** is a rule of the world (P6). The player doesn't own it; they *discover* it.
- **A recipe** is a *procedure the player writes* that makes use of one or more reactions: an ordered list of verbs, materials, arrangements and waiting periods that reliably produces a result.

How it works in the MVP:

1. **The journal keeps rumours apart from laws [R2].**
   - When the player first sees a reaction happen, the journal records it automatically as a **"?" observation**: what was there before, what came after, and the conditions seen.
   - Once the player has reproduced it, or measured its conditions with instruments, it becomes a **law**.
   - Entries flag "more to discover here" when the player has seen only some of a reaction's variants.
   - Either kind of entry is the reward for observing (Pillar 1: no action is wasted).
2. The player can **write recipes** in the journal by putting together steps, for example: *place clay in a stone enclosure → surround it with wood → ignite → wait → collect brick*.
3. **A saved recipe runs as a single action [R4].** It costs the materials plus time. This is where effort turns into leverage: thinking it through once lets the player repeat it cheaply. Recipes exist to take repetition out, so nothing in the game should require doing a known recipe by hand again.
4. Recipes can **nest** (a recipe can be a step in another recipe). This is how small discoveries add up to large, world-changing actions, such as building a dam, starting a controlled burn, or terraforming.
5. **Recipes are open-ended and scored [R12].**
   - Any arrangement that produces the result is valid.
   - Each recipe gets a score for yield, energy used and time taken, and is shown against a distribution, like Zachtronics histograms. In the MVP the distribution is the player's own earlier attempts; with sharing it becomes the community's.
   - "Commissions" add the constraints that keep freedom challenging, for example "make glass using under 200 units of heat".
6. **Recipes are never deleted or nerfed [R5].** If a rule change or a new world breaks a recipe, it is marked "unverified here", never removed.
7. **Recipes can be shared [R14].** A recipe exports to a short text code that can be imported elsewhere. An imported recipe stays "unverified" until it has run successfully in the player's own world.
8. **Insight produces spectacle [R13].** The first successful run of a new recipe gets a clear, visible payoff in the world, not just a line in a menu.

## 5. Randomized-rules mode

Decision D2: each world can randomize its rule *constants*, so knowledge of facts doesn't carry over between worlds, only knowledge of method does.

**Tiers (revised after research):** randomizing everything turned out to be expert-only. Noita randomizes only two alchemy recipes per world. NetHack-style identification is praised for tension but criticized as tedious.

| Tier | What changes | Audience |
|---|---|---|
| 0 — Standard | Nothing; fixed natural-science constants | First playthrough, learning the primitives |
| 1 — Shifted (default random mode) | 3–5 high-value constants, e.g. water's boiling point, one fuel's ignition temperature, one reaction's energy change | Returning players: relearn a few facts with familiar methods |
| 2 — Unknown world (expert) | All the constants listed below, plus optional obfuscation of material names | Players who want to learn everything from scratch |

**What can be randomized (within limits; all of it at Tier 2):** melting and boiling points, densities, conductivities, the energy change of each reaction, and possibly which of a set of candidate reactions exist at all.

**Relearning is done with instruments, not by trial and error [R7].**
- Each randomized constant can be measured: a thermometer to find a boiling point, a scale for density.
- The journal shows a **"possible values" readout** that narrows down as the player takes measurements.
- No constant can only be found by luck or by sacrificing materials repeatedly.

**Seed sharing:** world seeds are shareable at Tiers 0–1. Expect community calculators that work out a seed's constants, and treat them as a form of engagement. Tier 2 seeds are hidden by default, so the relearning stays real.

**What stays fixed:** the primitives (P1–P8), conservation, and the verbs. Players should be able to reason about a new world, not face arbitrary chaos.

**Optional obfuscation:** materials are shown by appearance only, with no names. The player names them in the journal.

**Balance safeguard:** every generated world has to pass an automated **viability check** before it's offered to the player. A headless simulation confirms that:

- water stays liquid somewhere in the normal surface temperature range,
- at least one fuel and ignition path exists,
- plants can grow somewhere,
- a defined set of "milestone" materials (such as glass, brick and metal) can be reached through some chain of reactions.

Worlds that fail are rerolled.

**Effect on recipes:** recipes written in one world may fail in another. That isn't a bug; it's what this mode is for. A recipe could be marked "verified in this world" once it has run successfully.

## 6. Permanence and preservation (D11, D14)

The world can be damaged permanently (D11). The research says permanence is tolerated when it is announced and caused by the player, and resented when it is silent or arbitrary.

- **Preview before irreversible change [R8].** Any single action or recipe that will change more than a set number of cells, or release more than a set amount of energy, first shows:
  - the area it will affect
  - the energy it will release
  
  The player confirms. Small actions are never interrupted.
- **Nothing is lost silently [R8].** There are no hidden deletions. Items inside something being destroyed are dropped into the world, not removed.
- **Every collapse can be traced [R8].** After a large event, the journal offers a short "what happened" trace: the chain of reactions and energy flows that caused it. That way a loss becomes something learned.
- **Snapshots and a fossil record [R9].**
  - The player can snapshot the world at any time, with a few slots in the MVP.
  - Named landmarks keep their journal entry and a picture after the cells themselves are destroyed.
  - This doesn't undo consequences. It lets players finish and keep what they made.
- **Spread is slow, visible and containable [R10].**
  - Anything that propagates (fire, erosion, later corruption or ecology) moves at a speed the player can see.
  - It can be stopped with materials the player understands, such as a firebreak or a wall.
  - There is an optional "pause spread" world setting.
  - Ruined ground should become something new to explore (ash makes soil fertile; cooled lava becomes new stone), not just dead cells.

## 7. Balance and measurement (D3)

The prototype should log enough to tell whether Pillar 1 holds up, and to check each design rule. The research-backed targets are in the table below.

- Effort spent, by type: time, number of actions, materials used, new reactions tried.
- Reward received, by type: new reactions discovered, recipes written, materials produced, and **world change**. One way to measure world change is the number of cells changed, weighted by how long they stay changed.
- Reward per unit of each effort type. D1 implies **insight should come out ahead of repetition**, with repetition still clearly above zero.

| Metric | Rule | Target / question |
|---|---|---|
| Time to first observed reaction; time to first saved recipe | R1 | Under 5 min; under 60 min |
| Share of "?" entries the player deliberately tests | R2 | Rising over a session |
| Experiments per hour; quitting after a failed experiment | R3 | High; low |
| Recipe reuse rate; share of recipes revised to be more efficient | R4, R12 | Recipes are reused, and improved |
| Hand-repeated sequences that already exist as a saved recipe | R4 | Near zero |
| Measurements per new world; time to re-verify core recipes | R7 (randomized mode) | Players measure rather than guess |
| Players who keep playing after a large event they caused; snapshot use | R8, R9 | Players keep playing after big losses |
| Frame time at full world size | R15 | ≤ 16.7 ms (60 fps) |

## 8. MVP placeholders (D5)

These are deliberately minimal for now: art (flat colour per material), sound, the goal or win condition (D10), UI polish, multiplayer, and the production engine (D12; the prototype runs in the browser). Snapshots and recipe sharing are no longer placeholders (D14). Saving whole worlds between sessions beyond those snapshots still is.

## 9. Open questions for this ruleset: proposed answers

These are proposals based on the research, pending confirmation:

1. **Should the player character be subject to the same rules?** *Proposed: yes, but losses are cheap.*
   - The character can be burned, drowned or buried. A special case would break R11.
   - Dying returns the player to their last camp, keeping the journal, recipes and the changed world. Only what they were carrying is dropped where they died.
   - Rationale: losses that feel meaningful are accepted and meaningless ones are resented; probes must stay cheap (R3).
2. **Should recipes run instantly, or play out in the world?** *Proposed: they play out in the world, sped up.*
   - The player sees the reactions happen, so a run can fail visibly. A failure gets a "what happened" trace (R8).
   - The first successful run is a moment of spectacle (R13).
   - Larger recipes are previewed first (R8).
3. **How big should the MVP world be?** *Proposed: 512×256 cells, adjusted to the performance budget (R15).* The first toy prototype uses a smaller grid (see [03-prototype-plan.md](03-prototype-plan.md)).

## Sources

- Falling-sand games (the cell-simulation model used here) — https://en.wikipedia.org/wiki/Falling-sand_game
- Cellular automaton — https://en.wikipedia.org/wiki/Cellular_automaton
- Noita (pixel-simulated world as gameplay) — https://en.wikipedia.org/wiki/Noita_(video_game)
- Conservation of energy — https://en.wikipedia.org/wiki/Conservation_of_energy
- Phase transition — https://en.wikipedia.org/wiki/Phase_transition
- Procedural generation (randomized worlds) — https://en.wikipedia.org/wiki/Procedural_generation
- Research behind rules R1–R16 — [../research/02-gameplay-loops-findings.md](../research/02-gameplay-loops-findings.md), [../research/03-review-mining-findings.md](../research/03-review-mining-findings.md)
- Noita alchemy (only two recipes randomized per seed) — https://noita.wiki.gg/wiki/Alchemy
- NetHack identification critique (Golden Krone Hotel) — https://www.goldenkronehotel.com/wp/2017/06/25/things-i-hate-about-roguelikes-part-2-identification/
- Zachtronics-style solution histograms (Exapunks) — https://en.wikipedia.org/wiki/Exapunks
- Terraria world-evil spread and its pause toggle — https://terraria.wiki.gg/wiki/Power_Menu
