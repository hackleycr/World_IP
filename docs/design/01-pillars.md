# Design Pillars — First Pass

Status: draft, updated 2026-10-20 with research findings. See the decision log (section 0) for what has been settled, and section 2a for the design rules the player research supports.

## 0. Decision log

| # | Topic | Decision |
|---|---|---|
| D1 | What counts as effort | Reward thinking above effort, but effort always counts for something. |
| D2 | Randomized-rules mode | Add a mode where each world's rule constants are randomized, so players have to learn reality from the ground up. **Revised after research:** randomization is tiered. The default changes a few high-value constants; "learn everything from scratch" is the expert tier. See [02-ruleset-mvp.md](02-ruleset-mvp.md#5-randomized-rules-mode). |
| D3 | Balance | Balance is a hard requirement. The conserved-quantity foundation (section 4) is the main tool for it, backed by measurement in the prototype. |
| D4 | Conserved-quantity foundation | Accepted as a working idea; revisit after prototyping. |
| D5 | Scope | Treat everything outside the core gameplay loop as an MVP placeholder, then iterate. |
| D6 | Research | Research the gameplay loops of popular games to quantify what players enjoy and what brings them back. See [../research/01-gameplay-loops.md](../research/01-gameplay-loops.md). |
| D7 | Perspective | 2D. |
| D8 | Setting | A basic natural-science world first; other domains can be added later. |
| D9 | How created actions are recorded | Recipes, to start with. |
| D10 | Goal | Deferred; leave it as an MVP placeholder for now. |
| D11 | Consequences | Actions have permanent consequences: the world can be damaged. |
| D12 | Team, engine, platform | Deferred until more research is done. The throwaway prototype is built in the browser (HTML canvas + JavaScript) because it is quickest to build and share; this does not decide the production engine. |
| D13 | Design rules from research | Adopt the design rules in section 2a as working requirements. Each rule is backed by [02-gameplay-loops-findings.md](../research/02-gameplay-loops-findings.md) and [03-review-mining-findings.md](../research/03-review-mining-findings.md), and each has a metric to test in the prototype. |
| D14 | Preservation and sharing | Saving snapshots of past world states and sharing recipes move from "placeholder" into the MVP, because the research ties both directly to Pillars 1–3 (see R9 and R14). |

## 1. The pillars, as stated

1. **Proportional reward.** The player is always rewarded in proportion to their effort.
2. **A malleable world.** The player's actions can and do change the environment, in small to extremely large ways.
3. **Discoverable rules.** The player can explore and create new kinds of actions and effects by understanding and manipulating the game's fundamental rules.

## 2. Sharpening each pillar

### Pillar 1: Proportional reward

"Effort" needs a definition, because the design changes depending on what we count. There are at least four kinds:

| Kind of effort | Example | Natural reward |
|---|---|---|
| **Time / repetition** | Gathering, building, travelling | Material accumulation, visible construction |
| **Skill / execution** | Precise timing, combat, navigation | Access, survival, style |
| **Understanding / insight** | Working out how two rules interact | New capabilities (Pillar 3) |
| **Risk** | Trying something that could backfire | Outsized outcomes, including big failures |

Proposed rules for this pillar:

- **Every input produces a visible output.** No action is wasted. A failed experiment still teaches something, leaves a mark, or yields material.
- **"Proportional" means it scales, not that it is linear.** Pure linear reward for time makes grinding the best strategy. Insight and risk should pay off more per unit than repetition does, but repetition should never pay nothing.
- **Rewards should be legible.** The player should be able to see why they got what they got, so the link between effort and reward teaches them something.

**The main tension (Pillar 1 vs. Pillar 3):** if a player finds a clever exploit that gets a huge result for a few seconds' work, is that disproportionate? The proposed answer is no: the insight is the effort. But the design needs a way to stop a single discovery from making all other effort pointless (see section 4, conservation).

### Pillar 2: A malleable world

- **One set of rules at every scale.** Kicking a stone and diverting a river should run on the same underlying rules, not on separate scripted systems. That is what makes large changes feel earned rather than handed out.
- **Changes persist.** If the player reshapes something, it stays reshaped, and the rest of the world reacts to it: creatures move, weather changes, other systems adapt.
- **Large change has knock-on effects.** The bigger the change, the more it spreads into other systems. This is where much of the late-game content comes from.

Risks to plan for:

- **Breaking the game.** If the player can destroy anything, they can destroy what they need. Options: accept it and make recovery part of the game, have the world regenerate, or protect a few key structures (which breaks the "one set of rules" idea).
- **Technical cost.** Persistent, simulated change at large scale is the hardest engineering problem in this design. It will decide the choice of 2D vs. 3D, world size, and engine.

### Pillar 3: Discoverable rules

- **Systemic, not authored.** Instead of hand-designing 200 spells or tools, design a small set of primitives (properties, forces, materials, verbs) that combine. New actions come from combining them.
- **Consistent and readable.** The player can only "understand" rules that never have special cases. Every exception we add makes reasoning about the world less reliable.
- **Knowledge counts as progress.** A player who understands the rules should be stronger than one who doesn't, even with the same items. Taken to its extreme, a skilled player could finish the game early because they know enough.
- **Discovered actions are real things in the game.** Once the player works out a new effect, they should be able to name it, save it, reuse it, refine it and (perhaps) share it. That needs some kind of *grammar*: runes, recipes, circuits, code, or gestures.

## 2a. Design rules from player research

These rules come from the research: 58 games compared, and 35,942 Steam reviews mined. Evidence and metrics are in [02-gameplay-loops-findings.md](../research/02-gameplay-loops-findings.md#recommendations-tied-to-the-three-pillars) ("rec." numbers) and [03-review-mining-findings.md](../research/03-review-mining-findings.md#4-what-this-changes-for-the-design). Where each rule shows up in the ruleset is in [02-ruleset-mvp.md](02-ruleset-mvp.md).

| # | Pillar | Rule | Key evidence |
|---|---|---|---|
| R1 | P1, P3 | **First insight in the first hour.** The starting area shows two or three phenomena the player can observe but that are not explained, and the player saves a first recipe early. | Negative reviewers of discovery games quit at a median of 5.8 h; onboarding is a cross-genre complaint topic (67% negative) |
| R2 | P3 | **The journal separates rumours from laws.** Observations are logged as "?" entries; confirmed reactions become laws. | Outer Wilds ship log; information-gap theory |
| R3 | P1 | **Experiments are cheap.** Small tests cost little and are easy to contain. Risk and energy cost apply to large-scale use. | Free undo in Baba Is You; Noita's "no safety net" complaint |
| R4 | P1 | **No repetition between two insights.** Recipes take the repetition out once the player understands something. New tiers change *what* the player does (new primitives, verbs, tools), not *how long* it takes. | In discovery games, grind is 3.5× (codebook) / 1.9× (union method) more frequent in negative reviews; Potion Craft "padded with filler" |
| R5 | P1 | **Never devalue past effort.** Rebalance by adding rules, never by nerfing or deleting recipes players own. | Diablo IV Season 14 backlash; Destiny 2 sunsetting; lost progress is 3.3× more frequent in negative reviews |
| R6 | P1 | **Unlocks widen capability** (instruments, verbs, precision). They do not raise stats. Any power boost is small and refundable. | Balatro and Slay the Spire breadth unlocks; Vampire Survivors refunds |
| R7 | P1, P3 | **Variation must be learnable, never a gamble.** Every random element can be worked out by experiment. Luck never gates the expressive toolkit. | The "RNG in card games" topic is 94% negative; Noita reviewers call wand luck "gambling" |
| R8 | P2 | **Signal permanence before it happens, and make it causal.** Large irreversible actions are previewed, showing the area affected and the energy cost. Nothing is ever lost silently. Collapses can be traced back to their cause. | Negative mentions of permanence are almost all unannounced lockouts or silent losses; losses that feel "meaningless" are what players resent |
| R9 | P2 | **Players can finish and keep their work:** snapshots, a "fossil record" of past world states, and named landmarks that outlive their cells. | The IKEA effect disappears when the creation is destroyed |
| R10 | P2 | **Spread is slow and visible, and can be contained.** Damage that spreads can be stopped, and ruined ground becomes new ecology to explore. | Terraria spread complaints and the pause toggle added later; Dwarf Fortress's "Losing is fun" |
| R11 | P3 | **Physics never breaks its own rules.** No special cases, including "structures that should collapse but don't". | Teardown complaints are about inconsistency, not destruction |
| R12 | P1, P3 | **Recipes are open-ended and scored.** Any valid solution works. Recipes are scored on yield, energy and time against a distribution. Freedom comes with constraints. | Zachtronics topic only 20% negative; "too unrestricted to be challenging" is the failure on the other side |
| R13 | P3 | **Insight produces spectacle:** a successful idea causes a visible, satisfying change in the world, not a quiet unlock. | The Strategy motivation has declined (Quantic Foundry); "Greatest game ever" topic is 8% negative |
| R14 | P3 | **Recipes can be shared** (export/import) to give players a social reason to play and to turn individual insight into community knowledge. | Self-determination theory's need to feel connected to others is otherwise unmet; Tears of the Kingdom build communities |
| R15 | All | **Simulation performance is a design priority.** Frame rate and stability count as gameplay. | Crashes are the largest cross-game topic (89% negative); bugs and performance are the top negative theme for sandbox games |
| R16 | P2, P3 | **Long-term re-engagement comes from new primitives** (electricity, pressure, wind…), not from content packs. | Factorio's and Satisfactory's record player counts years later came with releases that added new systems |

## 3. How the pillars fit together: the core loop

```
   Observe the world ──► Form a hypothesis about a rule
          ▲                         │
          │                         ▼
  New phenomena appear        Experiment (cheap, small scale)
          ▲                         │
          │                         ▼
  Change the world at a      Codify it as a new action
  larger scale        ◄───── (a reusable "recipe")
```

- Pillar 3 drives the left-to-right part: understanding turns into capability.
- Pillar 2 closes the loop: applying a capability changes the world, and the changed world reveals rules or interactions the player hadn't seen before.
- Pillar 1 runs through every step: each step pays out (knowledge, material, a new action, a visible change).

## 4. A candidate foundation: conservation

One idea that would serve all three pillars at once: **build the rules on a conserved quantity**, a resource that can be moved and transformed but not created from nothing. Call it energy, essence, mass or something else; the fiction can come later.

- **Proportional reward (P1):** big effects need big inputs, so effort is literally what powers change. The game's own accounting enforces proportionality instead of designer-tuned numbers.
- **Change at every scale (P2):** moving a pebble and moving a mountain differ only in how much of the quantity flows. The same rule covers both.
- **Discovery (P3):** cleverness becomes *leverage*: finding chains, catalysts or feedback loops that turn a small input into a large result by drawing on energy already stored in the world (a dammed river, a forest ready to burn, unstable ground). Insight is rewarded heavily, but it stays bounded because the energy has to come from somewhere, and using it changes the world.

This also resolves the tension in Pillar 1: an exploit isn't a bug if it spends stored potential the world really had. And once that potential is spent, it's gone, which is a consequence (Pillar 2).

## 5. Games worth studying

Each of these does part of what we want. None does all three.

| Game | Relevant to | What to take from it |
|---|---|---|
| Noita | P2, P3 | Every pixel simulated; wand-building as composable spell grammar |
| Breath of the Wild / Tears of the Kingdom | P3 | "Chemistry engine": a few consistent rules (fire, wind, electricity, physics) that combine; Ultrahand as player-built devices |
| Dwarf Fortress | P2 | Deep persistent simulation; the world reacts to and remembers the player |
| Minecraft (redstone) | P2, P3 | A small primitive set that players turned into full logic circuits |
| Teardown | P2 | Fully destructible voxel world; planning large-scale change is the gameplay |
| Magicka | P3 | Combining elements into spells as a real-time grammar |
| Baba Is You | P3 | The rules themselves are objects the player can manipulate |
| Outer Wilds | P1, P3 | Progress through knowledge only; the player's understanding is the upgrade |

## 6. Open questions (needed before the next design pass)

Resolved or deferred in the decision log: 1 → D7, 2 → D8, 3 → D9, 4 → D10, 6 → D11, 7 → D12. Question 5 (single-player or shared world) is partly answered: recipes are shared (D14), and the world remains single-player for the MVP.

1. **Perspective and dimension.** 2D (much cheaper to simulate at large scale, like Noita) or 3D?
2. **Fiction / setting.** Magic, science, a mix, or something abstract? This decides what the conserved quantity and the primitives *look like*.
3. **What is the "grammar" for created actions?** Runes / glyphs, physical contraptions, a visual programming language, gestures, recipes?
4. **Is there a goal?** Open-ended sandbox, or a structured objective (survival, restoring or reshaping a world, an antagonist)?
5. **Single-player or shared world?** Shared discoveries and a persistent shared world would amplify Pillars 2 and 3, but add a lot of scope.
6. **Is the world allowed to be ruined?** Permanent consequences, regeneration, or something in between?
7. **Team, engine, platform and timeline.** Solo hobby project or a team? Is there an engine preference (Godot, Unity, Unreal, Bevy, custom)?

## 7. Suggested next steps

1. ~~Answer the open questions above, at least 1–4.~~ Done (decision log).
2. ~~Draft the **primitive set**.~~ Done: 8 primitives in [02-ruleset-mvp.md](02-ruleset-mvp.md).
2a. ~~Research gameplay loops and player sentiment.~~ Done: [02](../research/02-gameplay-loops-findings.md) and [03](../research/03-review-mining-findings.md).
3. **Next:** build a **throwaway toy prototype**. The plan is in [03-prototype-plan.md](03-prototype-plan.md). (a 2D grid sandbox is the cheapest) to test one thing only: *is it fun to discover how two or three primitives interact?* That is the riskiest assumption in the whole design, so test it first.
4. Only after that, design progression, setting and content.

## Sources

**Player research behind section 2a** (full source lists inside each report)
- First-pass research report — [../research/02-gameplay-loops-findings.md](../research/02-gameplay-loops-findings.md)
- Steam review mining report — [../research/03-review-mining-findings.md](../research/03-review-mining-findings.md)
- Steam reviews endpoint (data source) — https://store.steampowered.com/appreviews/881100?json=1
- IKEA effect (Norton, Mochon & Ariely) — https://papers.ssrn.com/abstract=1777100
- Outer Wilds ship log analysis — https://paigecuthbertson.com/pdfs/The_Ship_Log_in_Outer_Wilds.pdf
- Noita alchemy randomization — https://noita.wiki.gg/wiki/Alchemy
- Factorio Space Age player record — https://gamingonlinux.com/2024/10/factorio-space-age-sold-over-400000-copies-and-sets-a-new-player-count-record

**Design concepts**
- Emergent gameplay — https://en.wikipedia.org/wiki/Emergent_gameplay
- Immersive sim (systemic design tradition) — https://en.wikipedia.org/wiki/Immersive_sim
- Cellular automaton (basis of falling-sand / pixel-simulation worlds) — https://en.wikipedia.org/wiki/Cellular_automaton
- Flow (psychology), on matching challenge to skill — https://en.wikipedia.org/wiki/Flow_(psychology)
- Self-determination theory (competence and autonomy as motivators) — https://en.wikipedia.org/wiki/Self-determination_theory

**Reference games**
- Noita — https://en.wikipedia.org/wiki/Noita_(video_game)
- The Legend of Zelda: Breath of the Wild — https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Breath_of_the_Wild
- The Legend of Zelda: Tears of the Kingdom — https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Tears_of_the_Kingdom
- Dwarf Fortress — https://en.wikipedia.org/wiki/Dwarf_Fortress
- Minecraft — https://en.wikipedia.org/wiki/Minecraft
- Teardown — https://en.wikipedia.org/wiki/Teardown_(video_game)
- Magicka — https://en.wikipedia.org/wiki/Magicka
- Baba Is You — https://en.wikipedia.org/wiki/Baba_Is_You
- Outer Wilds — https://en.wikipedia.org/wiki/Outer_Wilds
