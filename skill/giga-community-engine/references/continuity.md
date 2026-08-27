# Storyboard, Episode, and Repair Continuity

## Scene-state ledger

Maintain this compact state internally after every approved frame or board:

```text
GIGA: face | hair | beard | physique | wardrobe | pose | condition
SECONDARIES: identity block | wardrobe | position | condition
WORLD: location | time | weather | light | damage | persistent marks
PROPS: owner | position | orientation | condition
GEOGRAPHY: screen direction | entrances/exits | camera side | landmarks
ACTION: completed | current | unresolved | next plausible beat
STYLE: era selection source | target build | geometry budget | texture/filtering/UV
STYLE: materials/lighting | effects/draw distance | camera/capture grammar | aspect
GROUNDING: screenshot-reference set | source quality | rendering contract | gate result
AUTHORITY: identity ref | latest approved image | approved shot/board
```

The latest approved state outranks the original premise for continuity. The identity reference still controls face, hair, beard, physique, and silhouette.

## Shot construction

Give every shot one job: hook, reveal, action, reaction, transition, escalation, payoff, portrait, or loop closure.

- default cinematic: 5-7 connected shots unless the action needs fewer
- vary scale and perspective: wide geography, low/high angle, lateral action, insert/detail, close reaction, consequence
- do not repeat near-identical medium three-quarter compositions
- maintain eyelines, screen direction, object ownership, relative positions, and action phase
- show causal transitions; do not teleport characters or reset damaged/used props
- keep camera motion motivated and readable; dynamic does not mean chaotic

## Approval gates

### First frame

Lock identity, wardrobe, environment, era-selection source, screenshot-reference set, rendering contract, camera geography, and current action.

### Storyboard

Check each panel against the previous panel and the approved rendering contract, then check the contact sheet as one sequence. Approval locks shot order and end-state. No panel may become sharper, denser, more cinematic, or more modern than the active build.

### Animation

Animate from the approved storyboard/reference and rendering contract only. Do not redesign characters, modernize materials or lighting, invent new props, add unrequested dialogue/text/music, or change the story during motion.

## Episode progression

Default to four progressive storyboards:

1. **Hook + Setup** — begin with the premise already active; establish only what the viewer needs
2. **Escalation / Development** — deepen the same conflict or objective
3. **Major Development / Turn** — materially alter stakes, knowledge, location state, or character position
4. **Payoff / Resolution** — resolve the central visual promise and preserve a clear final state

Use Board 5 only when structurally justified for aftermath, second payoff, loop closure, or a necessary final turn. Do not use it merely to add more shots.

Workflow:

```text
CONCEPT -> BOARD 1 -> APPROVAL -> UPDATE LEDGER
-> BOARD 2 FROM BOARD 1 END-STATE -> APPROVAL -> UPDATE LEDGER
-> BOARD 3 FROM BOARD 2 END-STATE -> APPROVAL -> UPDATE LEDGER
-> BOARD 4 FROM BOARD 3 END-STATE -> APPROVAL
-> OPTIONAL BOARD 5 ONLY IF JUSTIFIED -> ANIMATION PACKAGING
```

Never generate all boards from the original concept independently. Carry visible changes, missing/used props, injuries, debris, weather, time, positions, and unresolved actions forward.

## Multi-character rules

- assign one identity block and reference role per character
- state who occupies left/right/foreground/background when geography matters
- describe contact points explicitly during interaction
- keep wardrobe and anatomy traits isolated
- avoid merging faces, sharing beards, copying GIGA's physique, or duplicating subjects

## Failure diagnosis

Classify the smallest failed layer:

1. identity
2. anatomy/count
3. continuity/state
4. geography/orientation
5. action readability
6. target fidelity or wrong-era drift
7. camera variety
8. atmosphere/decorative detail

Repair the earliest failed layer first. Treat wrong-era construction as a structural failure before atmosphere or decorative detail. Preserve approved layers in an explicit LOCK / CHANGE ONLY / DO NOT CHANGE block. If one panel fails, replace that panel rather than rebuilding the entire board whenever practical.
