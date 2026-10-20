# Design Pillars — First Pass

Status: draft for discussion. Nothing here is settled except the three pillars themselves.

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

1. **Perspective and dimension.** 2D (much cheaper to simulate at large scale, like Noita) or 3D?
2. **Fiction / setting.** Magic, science, a mix, or something abstract? This decides what the conserved quantity and the primitives *look like*.
3. **What is the "grammar" for created actions?** Runes / glyphs, physical contraptions, a visual programming language, gestures, recipes?
4. **Is there a goal?** Open-ended sandbox, or a structured objective (survival, restoring or reshaping a world, an antagonist)?
5. **Single-player or shared world?** Shared discoveries and a persistent shared world would amplify Pillars 2 and 3, but add a lot of scope.
6. **Is the world allowed to be ruined?** Permanent consequences, regeneration, or something in between?
7. **Team, engine, platform and timeline.** Solo hobby project or a team? Is there an engine preference (Godot, Unity, Unreal, Bevy, custom)?

## 7. Suggested next steps

1. Answer the open questions above, at least 1–4.
2. Draft the **primitive set**: the smallest list of properties, forces and interactions that could produce interesting combinations. Aim for 6–12 primitives.
3. Build a **throwaway toy prototype** (a 2D grid sandbox is the cheapest) to test one thing only: *is it fun to discover how two or three primitives interact?* That is the riskiest assumption in the whole design, so test it first.
4. Only after that, design progression, setting and content.

## Sources

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
