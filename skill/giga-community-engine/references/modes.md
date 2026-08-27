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

## Grounded-build prefix

Before generating in STILL, SCENE, CLASSIC CINEMATIC, image-based TRAINING, COMMERCIAL, or EPISODE, resolve the active build. When gameplay grounding is triggered, follow [rendering-grounding.md](rendering-grounding.md) through screenshot inspection, reference assignment, rendering contract, and the identity + fidelity gate. Do not show or expand a frame that fails the gate.

## CHARACTER

```text
REFERENCE ASSIGNMENT -> IDENTITY STUDY -> LIKENESS CHECK -> NARROW REPAIR
```

Default to one neutral study or a clean multi-view sheet only when requested. Avoid building lore, scenery, or animation around a pure identity request.

## STILL

```text
IDEA -> ACTIVE BUILD / IMAGE DIRECTION -> OPTIONAL GROUNDING -> IMAGE
-> REQUIRED GATE WHEN GROUNDED -> REPAIR OR VARIATION
```

Create one strong image. Do not add storyboard or video packaging unless requested. If the user later says `turn this into a scene`, promote the approved still to project authority.

## MEME

```text
IDEA -> ONE-GLANCE PREMISE -> IMAGE OR COPY-PASTE PROMPT -> OPTIONAL CAPTION
```

Default to visual-first legibility. If exact text matters, preserve clean caption space or provide copy separately rather than trusting generated typography.

## SCENE

```text
IDEA -> ACTIVE BUILD -> OPTIONAL GROUNDING -> FIRST FRAME
-> REQUIRED GATE WHEN GROUNDED -> APPROVAL -> 3-5 SHOT PLAN OR ONE-TAKE BRIEF
-> APPROVAL WHEN NEEDED -> ANIMATION PROMPT
```

Use one clear event and approximately 6-12 seconds by default. Do not inflate a tiny gag into a full cinematic.

## CLASSIC CINEMATIC

```text
CONCEPT -> ACTIVE BUILD -> OPTIONAL GROUNDING -> GENESIS FRAME
-> REQUIRED GATE WHEN GROUNDED -> APPROVAL -> 5-7 SHOT STORYBOARD
-> APPROVAL -> MODEL-NEUTRAL MOTION BRIEF -> PROVIDER PROMPT
```

If the premise is clear, choose one strong direction and create the genesis frame. If development is needed, offer no more than three concise concepts. Treat the approved genesis frame as visual authority for the storyboard.

## TRAINING / SELF-IMPROVEMENT

Use STILL, SCENE, or CLASSIC CINEMATIC mechanics based on scope, including their grounded-build prefix. Show effort, practice, consistency, recovery, preparation, or proof of work. Keep technique and equipment visually plausible. Do not make medical, hormonal, supplement, or guaranteed-performance claims.

## COMMERCIAL

```text
HOOK -> PRODUCT/SERVICE NEED -> FICTIONAL SOLUTION -> DEMONSTRATION
-> PAYOFF -> OPTIONAL LOGO/END CARD
```

For a full spot:

```text
CONCEPT -> SCRIPT IF NEEDED -> NARRATION ROUTE -> ACTIVE BUILD
-> OPTIONAL GROUNDING -> FIRST FRAME -> REQUIRED GATE WHEN GROUNDED -> APPROVAL
-> STORYBOARD -> APPROVAL -> ANIMATION PACKAGE
```

Treat the absurd product seriously. Keep the offer visually readable. Use in-model narration, separate voiceover, none, or automatic; prefer separate voiceover when exact delivery matters.

## EPISODE

Use the progressive four-board workflow in [continuity.md](continuity.md). Resolve and ground the build before Board 1 when triggered, then preserve the approved rendering contract through every later board. Default to Board 1 Hook + Setup, Board 2 Escalation, Board 3 Major Turn, and Board 4 Payoff. Add Board 5 only when justified. Approve and lock each board before advancing.

## Output discipline

- generate when generation tooling is available and requested
- return prompt-only output when requested or generation is unavailable
- never claim video was rendered when only a prompt was produced
- keep creator-facing explanations short
- when exact limits apply, count the final prompt after all edits
