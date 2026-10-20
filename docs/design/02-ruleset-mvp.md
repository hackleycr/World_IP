# MVP Ruleset — 2D Natural Science

Status: first draft. It follows decisions D1–D11 in [01-pillars.md](01-pillars.md#0-decision-log).

The MVP has one job: show that **finding out how simple natural rules interact, and turning that into recipes, is fun**. Anything that doesn't serve that is a placeholder.

## 1. The world model

- **A 2D grid of cells**, side-on view, in the style of falling-sand games. Each cell holds one material plus a few state values.
- **Per-cell state:** `material`, `temperature`, `moisture` (optional for the MVP), and `age` (used for growth and decay).
- **Simulation tick:** each cell updates based on its own state and its 8 neighbours. Every rule is local; large-scale effects come from local rules adding up. That is Pillar 2's "one set of rules at every scale".

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

**Conservation (from section 4 of the pillars doc):** heat energy is conserved inside the simulation. It enters only through P8 and leaves only through slow radiation into the sky. Every reaction in P6 declares its energy change explicitly. This is the main balance lever (D3).

Deliberately left out of the MVP: electricity, pressure, magnetism, wind and light as a simulated quantity. Each is a candidate expansion once the core is shown to work.

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

### Recipes

There are two different things here, and keeping them apart matters:

- **A reaction** is a rule of the world (P6). The player doesn't own it; they *discover* it.
- **A recipe** is a *procedure the player writes* that makes use of one or more reactions: an ordered list of verbs, materials, arrangements and waiting periods that reliably produces a result.

How it works in the MVP:

1. When the player first sees a reaction happen, the **journal** records it automatically. That's the reward for observing (Pillar 1: no action is wasted).
2. The player can **write recipes** in the journal by putting together steps, for example: *place clay in a stone enclosure → surround it with wood → ignite → wait → collect brick*.
3. A saved recipe can be **executed** as one action, at a cost of the materials plus time. This is where effort turns into leverage: thinking it through once lets the player repeat it cheaply.
4. Recipes can **nest** (a recipe can be a step in another recipe). This is how small discoveries add up to large, world-changing actions, such as building a dam, starting a controlled burn, or terraforming.

## 5. Randomized-rules mode

Decision D2: each world can randomize its rule *constants*, so knowledge of facts doesn't carry over between worlds, only knowledge of method does.

**What gets randomized (within limits):** melting and boiling points, densities, conductivities, the energy change of each reaction, and possibly which of a set of candidate reactions exist at all.

**What stays fixed:** the primitives (P1–P8), conservation, and the verbs. Players should be able to reason about a new world, not face arbitrary chaos.

**Optional obfuscation:** materials are shown by appearance only, with no names. The player names them in the journal.

**Balance safeguard:** every generated world has to pass an automated **viability check** before it's offered to the player. A headless simulation confirms that:

- water stays liquid somewhere in the normal surface temperature range,
- at least one fuel and ignition path exists,
- plants can grow somewhere,
- a defined set of "milestone" materials (such as glass, brick and metal) can be reached through some chain of reactions.

Worlds that fail are rerolled.

**Effect on recipes:** recipes written in one world may fail in another. That isn't a bug; it's what this mode is for. A recipe could be marked "verified in this world" once it has run successfully.

## 6. Balance and measurement (D3)

The prototype should log enough to tell whether Pillar 1 holds up:

- Effort spent, by type: time, number of actions, materials used, new reactions tried.
- Reward received, by type: new reactions discovered, recipes written, materials produced, and **world change**. One way to measure world change is the number of cells changed, weighted by how long they stay changed.
- Reward per unit of each effort type. D1 implies **insight should come out ahead of repetition**, with repetition still clearly above zero.

## 7. MVP placeholders (D5)

These are deliberately minimal for now: art (flat colour per material), sound, the goal or win condition (D10), UI polish, saving beyond a single world, multiplayer, and the engine choice (D12; prototype in whatever is quickest).

## 8. Open questions for this ruleset

1. Should the player character be subject to the same rules, for example taking heat damage, drowning, or being buried? That would be consistent with Pillar 3, but it adds risk.
2. Should recipe execution be instant, or play out step by step in the world so it can go wrong?
3. How big should the MVP world be? (A suggested starting point is 512×256 cells.)

## Sources

- Falling-sand games (the cell-simulation model used here) — https://en.wikipedia.org/wiki/Falling-sand_game
- Cellular automaton — https://en.wikipedia.org/wiki/Cellular_automaton
- Noita (pixel-simulated world as gameplay) — https://en.wikipedia.org/wiki/Noita_(video_game)
- Conservation of energy — https://en.wikipedia.org/wiki/Conservation_of_energy
- Phase transition — https://en.wikipedia.org/wiki/Phase_transition
- Procedural generation (randomized worlds) — https://en.wikipedia.org/wiki/Procedural_generation
