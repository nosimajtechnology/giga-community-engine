# Modes and Production Workflows

## Routing

| User intent | Mode |
| --- | --- |
| turnaround, expression study, canonical portrait, identity check | CHARACTER |
| one image, poster, cover, screenshot, product shot | STILL |
| reaction, comparison, caption concept, fast community post | MEME |
| one progressing action or short connected sequence | SCENE |
| first-frame → storyboard → animation workflow | CLASSIC CINEMATIC |
| fitness, discipline, work, accountability, self-improvement | TRAINING / SELF-IMPROVEMENT |
| fictional brand, product, service, spot, ident | COMMERCIAL |
| long-form story across progressive boards | EPISODE |

Mode describes workflow, not tone. A TRAINING scene can be deadpan or surreal; a STILL can be photographic or PS1.

## Style-resolution prefix

Before generating in CHARACTER, STILL, MEME, SCENE, CLASSIC CINEMATIC,
image-based TRAINING, COMMERCIAL, or EPISODE, resolve the active style through
[style-adapters.md](style-adapters.md). When a registered adapter is active,
follow its reference assignments, rendering lock, motion rules, and repair
gate. When flagship PS2 or another game build is active, follow
[rendering-grounding.md](rendering-grounding.md) through screenshot inspection,
reference assignment, rendering contract, and the identity + fidelity gate.
Do not show or expand a frame that fails the selected gate.

## CHARACTER

```text
STYLE RESOLUTION -> REFERENCE ASSIGNMENT -> IDENTITY STUDY
-> LIKENESS + STYLE CHECK -> NARROW REPAIR
```

Default to one neutral study or a clean multi-view sheet only when requested. Avoid building lore, scenery, or animation around a pure identity request.

## STILL

```text
IDEA -> STYLE / IMAGE DIRECTION -> OPTIONAL GAMEPLAY GROUNDING -> IMAGE
-> REQUIRED SELECTED-STYLE GATE -> REPAIR OR VARIATION
```

Create one strong image. Do not add storyboard or video packaging unless requested. If the user later says `turn this into a scene`, promote the approved still to project authority.

## MEME

```text
IDEA -> STYLE -> ONE-GLANCE PREMISE -> IMAGE OR COPY-PASTE PROMPT
-> OPTIONAL CAPTION
```

Default to visual-first legibility. If exact text matters, preserve clean caption space or provide copy separately rather than trusting generated typography.

## SCENE

```text
IDEA -> STYLE -> VIDEO APPROACH WHEN AMBIGUOUS -> ROUTE WORKFLOW
```

Use one clear event and approximately 6-12 seconds by default. Do not inflate a
tiny gag into a full cinematic. CLASSIC CONTROL creates and approves a Genesis
Frame and shot plan before I2V. DIRECT EXPLORE produces a fully descriptive,
reference-free T2V concept. CHARACTER LOCK uses the canonical sheet as primary
R2V identity authority without fixing the opening frame.

## CLASSIC CINEMATIC

```text
CONCEPT -> STYLE -> OPTIONAL GAMEPLAY GROUNDING -> GENESIS FRAME
-> REQUIRED SELECTED-STYLE GATE -> APPROVAL -> 5-7 SHOT STORYBOARD
-> APPROVAL -> MODEL-NEUTRAL MOTION BRIEF -> PROVIDER PROMPT
```

If the premise is clear, choose one strong direction and create the genesis frame. If development is needed, offer no more than three concise concepts. Treat the approved genesis frame as visual authority for the storyboard.

For H3 Max this mode automatically selects CLASSIC CONTROL. Upload the approved
Genesis Frame as the literal I2V opening frame. The storyboard controls planning,
shot order, geography, action states, and transitions but is not uploaded by
default. Read `model-adapters/fal-h3-max.md` for packaging.

## H3 Max creation routes

Resolve the route after style and before concept development or generation.
Skip the chooser when the user already named a route or their wording makes one
clear.

- **CLASSIC CONTROL:** optimized seed -> GPT Image 2 Genesis Frame -> gate ->
  approval -> GPT Image 2 storyboard -> approval -> H3 Max I2V.
- **DIRECT EXPLORE:** optimized concept -> H3 Max T2V with no references. A
  loose seed may receive up to three distinct concepts; a clear seed gets one
  refined direction.
- **CHARACTER LOCK:** optimized concept -> H3 Max R2V with the canonical GIGA
  sheet first, selected style sheet second when active, and only necessary
  role-limited additional references.

## TRAINING / SELF-IMPROVEMENT

Use STILL, SCENE, or CLASSIC CINEMATIC mechanics based on scope, including
their style-resolution prefix. Show effort, practice, consistency, recovery,
preparation, or proof of work. Keep technique and equipment visually plausible.
When Late-Z is active, use `TRAINING_BURST` when the action calls for an
explosive technique. Do not make medical, hormonal, supplement, or
guaranteed-performance claims.

## COMMERCIAL

```text
HOOK -> PRODUCT/SERVICE NEED -> FICTIONAL SOLUTION -> DEMONSTRATION
-> PAYOFF -> OPTIONAL LOGO/END CARD
```

For a full spot:

```text
CONCEPT -> SCRIPT IF NEEDED -> NARRATION ROUTE -> STYLE
-> OPTIONAL GAMEPLAY GROUNDING -> FIRST FRAME -> REQUIRED SELECTED-STYLE GATE -> APPROVAL
-> STORYBOARD -> APPROVAL -> ANIMATION PACKAGE
```

Treat the absurd product seriously. Keep the offer visually readable. Use in-model narration, separate voiceover, none, or automatic; prefer separate voiceover when exact delivery matters.

## EPISODE

Use the progressive four-board workflow in [continuity.md](continuity.md).
Resolve the style before Board 1. Preserve the approved adapter rules or
gameplay rendering contract through every later board. Default to Board 1 Hook
+ Setup, Board 2 Escalation, Board 3 Major Turn, and Board 4 Payoff. Add Board 5
only when justified. Approve and lock each board before advancing.

## Output discipline

- generate when generation tooling is available and requested
- return prompt-only output when requested or generation is unavailable
- never claim video was rendered when only a prompt was produced
- keep creator-facing explanations short
- when exact limits apply, count the final prompt after all edits
