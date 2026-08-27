# Model-Independent Prompt Adapters

## Core stack

Build every request from:

```text
CANON
+ APPROVED SCENE STATE
+ MODE
+ SCREENSHOT-DERIVED RENDERING CONTRACT WHEN ACTIVE
+ SHOT OR MOTION LOGIC
= MODEL-NEUTRAL BRIEF
-> PROVIDER ADAPTER
```

Provider names must not alter canon, story, or continuity. Change only syntax, length, reference assignment, and controls verified for the selected interface.

When gameplay grounding is active, the provider prompt must preserve the selected build's geometry budget, texture/filtering/UV behavior, materials and lighting, effects density, draw distance, camera grammar, and capture characteristics. Avoid generic adapter language such as `cinematic lighting`, `volumetric`, `ultra-detailed`, `photoreal materials`, bokeh, or modern depth of field unless the inspected build supports it.

## Image-generation adapter

Include:

1. identity reference assignment
2. subject construction and protected traits
3. current wardrobe/action/state
4. environment and spatial composition
5. grounded style observations
6. lighting, camera, and aspect ratio
7. decisive exclusions

When reference images are supported, assign each one a role. Do not tell a model to blend all references.

## Image-to-video adapter

Include:

1. approved start frame or storyboard as visual authority
2. duration and shot structure
3. one continuous action progression
4. character/object motion and contact points
5. camera movement per shot
6. continuity locks and end-state
7. target game-engine motion/rendering behavior
8. negatives: no redesign, duplicates, extra limbs, unrequested text/dialogue/music, state resets

Keep appearance descriptions concise when the approved image already carries identity. Spend prompt budget on motion, geography, and continuity.

## Seedance

Use storyboard/reference-first packaging when the current interface supports it. Write chronological shot beats with explicit transitions and a decisive final state. Keep camera direction dynamic but readable. Do not invent exact duration, aspect, audio, or reference-slot controls; verify the current interface or label them variable.

## Kling

Favor a clear start image, action verb, subject motion, environment response, camera motion, and endpoint. For multiple shots, maintain explicit screen direction and continuity. Verify current model/version controls rather than assuming feature parity.

## Sora

Describe one coherent world-state and temporal progression. Use shot language only when the selected Sora interface accepts or benefits from it. Avoid conflicting simultaneous instructions. Verify current access, duration, reference, audio, and storyboard capabilities.

## Higgsfield

Treat Higgsfield as an orchestration/interface layer whose available models and controls can change. Select the underlying image or video model first, then adapt to verified fields. Do not claim all Higgsfield models share the same prompt grammar.

## Generic/future adapter

If capabilities are unknown, provide:

```text
INPUT: approved image/storyboard
DURATION: user requirement or flexible
ACTION: chronological motion beats
CAMERA: readable motivated movement
CONTINUITY: protected state and endpoint
STYLE: observed era/build behavior
NEGATIVES: only decisive failure prevention
```

Mark unsupported specifics `unverified or variable`.

## Prompt-length compression

When the user sets an exact character limit, measure after final edits. Preserve in this order:

1. identity and anatomy
2. approved state and shot progression
3. contact points and continuity
4. target fidelity and screenshot-derived rendering contract
5. motion and camera
6. decisive negatives
7. atmosphere

Remove repetition, adjectives, and ornamental explanation first. Report the exact final character count.

## Delivery format

```text
SETUP: [one line]
REFERENCES: [role for each input]
PROMPT: [copy-paste prompt]
FIELDS: [only verified interface settings]
CHARACTER COUNT: [when requested]
```
