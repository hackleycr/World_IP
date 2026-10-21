# Prototype 0 — "Is discovery fun?"

Status: v0.5 (recipes fixed, geology) built 2026-10-21 after playtests [01 and 02](../playtests/2026-10-20-playtest-01.md) — [prototype/index.html](../../prototype/index.html). Throwaway: it exists to answer one question, and its code is not the production base (D12).

## The question

**Is it fun to discover how a few natural rules interact, and to capture that as a recipe?** ([01-pillars.md](01-pillars.md#7-suggested-next-steps), step 3.) Everything else is out of scope.

## What is in it

| Area | v0 scope | Rules |
|---|---|---|
| World | 240×135 cell side-view grid. Terrain: hills, a pond over a warm spring (lava below), an ice-capped mountain (air gets colder with altitude), a smouldering campfire beside a line of plants, a sand dune, clay, and ore veins | R1 (three phenomena to notice) |
| Simulation | Movement of powders, liquids and gases; density; heat that is conserved as it diffuses; hot air rising (flames are glowing hot air, not a special effect); phase changes with latent heat; about 20 reactions, each with a declared energy change; plant growth; deep-earth heat input; air exchanging heat with the sky | P1–P8, R11 |
| Progression by knowledge | The torch only heats to about 350°. Higher temperatures need insight: charcoal fires (~1100°) or lava. Glass, metal and brick sit behind chains of reactions | P1, R6 |
| Journal | A reaction seen for the first time becomes a **"?" observation**. When the player causes it, it becomes a **law**. Each entry records the temperatures measured. The journal shows the count of undiscovered reactions | R2 |
| Unlocks | Discovering a material adds it to the paint palette. Unlocks are capabilities only | R6 |
| Recipes | Record brush and torch strokes relative to a starting point, name them, then replay them anywhere as a single action, at 3× speed in the world. Each run measures its yield (crafted materials made in the area within 10 s) and keeps a history of past runs. Recipes export and import as text codes | R4, R12, R14 |
| Snapshots | Three save slots for the whole world | R9 |
| Randomized rules | Tier 0 (standard) or Tier 1 (4 shifted constants, constrained so the world stays viable). The journal shows the measured temperatures, so the player can work out the shifted values | D2, R7 |
| Metrics | Time to the first reaction seen, first one caused by the player, first law and first recipe; experiments; recipe runs; energy injected vs. energy released by chemistry. Exportable as JSON | Section 7 of the ruleset |

## Known simplifications (deliberate, for v0)

- **No player character:** the player acts directly with a cursor brush. Base materials are free to paint, so effort and conservation are only partly tested here; insight-gating is what's tested.
- **Rigid solids are fixed in place** (as in Noita). There is no structural collapse yet. This is a known exception to R11, listed so it gets fixed and not forgotten.
- **No preview before large actions (R8),** no "what happened" trace and no spread controls. These come later, once v0 shows that discovery itself is fun.
- **Tier 1's viability check** is a set of constraint checks on the constants, not a full simulation run without graphics.

## How to evaluate it

1. Have 3–5 people play for 20 minutes each, with no instructions beyond the controls.
2. Record the metrics export, and ask three questions:
   - What did you figure out?
   - What did you want to try next?
   - When were you bored?
3. Pass/fail signals:
   - **Pass:** the first player-caused reaction comes within 5 minutes; at least one recipe is saved; players describe chains of reactions they worked out ("I made charcoal to get the fire hot enough for…").
   - **Fail:** players paint pictures instead of experimenting; they can't tell why something happened; they stop after seeing the first few reactions.

## Version history

| Version | What changed | Why |
|---|---|---|
| v0 | First build | Test the core question |
| v0.2 | Labels showing reactions on the map, a cursor readout, recipes saved by working backwards from a result, discovery cards, hints | Playtest 01 feedback |
| v0.3 | **Climate:** humidity, evaporation, clouds and rain; wind from an ocean beyond the east edge, deflected upward by terrain; plants that move soil water into the air and wilt without it; humidity view; rain gauge; climate panel (wind, ocean humidity, rain by region, water budget, questions to investigate). Also: fires quenched by water dump their heat into it, and charcoal relights only with real air | Playtest 01 requests (deserts, mountains, forests); the player chose climate first |

| v0.3.1 | Wet fuel can't ignite (fixes a quench/relight loop); a labelled rain-gauge strip; a wind indicator | Playtest 03 |
| v0.4 | **Plants and soil:** water soaks into and drains through ground (sand, dirt, soil, mud); three species (grass, cactus, tree) with different water needs, chosen by where a seed lands; plants spread seeds downwind, drink from their roots, wilt, drown, and rot into **soil**; roots and ash turn sand or dirt into soil (succession); dormant seeds in the desert; wild seeds blowing in; the water view shows ground moisture; a "Living things" goal list with hints. Rain gauge is a rolling 60 s window with a Reset button | Playtest 04: "plants are fun, let's do more"; the gauge kept stale data |

| v0.5 | **Recipes:** working backwards now keeps only strokes that landed on or within 5 cells of the cells actually made; runs of the same stroke merge into one step with a duration (held torch = 1 step); only results that take real work offer a save (charcoal, glass, brick, metal, ice, soil, rocks). **Geology:** a pressure field (the weight above each cell); seven rocks (sandstone, shale, basalt, granite, obsidian, quartzite, slate) formed by burial, cooling environment, and heat under load; weathering by water and freeze–thaw; exposed lava radiates and flash-boils water; tooltip shows load; Discoveries panel groups materials, rocks and living things | Playtest 05: the "Make ash" recipe had 253 steps and was never run; the player asked for recipes first, then geology |

**Verified headlessly for v0.5:**
- A charcoal kiln built amid unrelated strokes gives a 26-step recipe (25 paint strokes plus 1 torch step) instead of hundreds, and replaying it elsewhere makes charcoal.
- Sandstone forms at the base of the dune and granite around the lava chamber, with no player action.
- In controlled set-ups:
  - lava in open air → basalt (23–28 cells)
  - lava with water poured on → obsidian (36–44 cells)
  - charcoal fire against buried sandstone → quartzite (8 cells; the sandstone reached 832°)
  - lava against buried shale → slate (3 cells)
- Regression checks pass: charcoal, ice, metal, the rain shadow and desert succession. A step takes 2.1–2.3 ms, with no errors.

**Verified headlessly for v0.4:**
- With light, steady watering of the desert, cacti establish first, their roots turn sand into soil (2 → 56 cells in 5 minutes), and grass follows (3 → 20).
- Flooding drowns plants, and they rot into soil.
- A step takes 1.7–2.0 ms, with no errors.

**Verified headlessly for v0.3:**
- Water is conserved over 5 minutes: water cells stay at 350–390.
- Rain concentrates on the windward slope. Flattening the mountain moves it into the valley: 71 vs. about 3 cells' worth, over 3 minutes.
- The earlier chains (charcoal, glass, brick, metal, ice) still work.
- Speed: 1.7–2.0 ms per step.
