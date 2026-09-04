# Model-Independent Prompt Adapters

## Core stack

Build every request from:

```text
CANON
+ APPROVED SCENE STATE
+ MODE
+ SELECTED STYLE ADAPTER OR SCREENSHOT-DERIVED RENDERING CONTRACT
+ REFERENCE-ROLE MAP
+ MOTION PROFILE AND STATE-CHANGE DELTA WHEN ACTIVE
+ MODEL-NEUTRAL ANIMATION BRIEF
= MODEL-NEUTRAL BRIEF
-> PROVIDER ADAPTER
```

Provider names must not alter canon, story, or continuity. Change only syntax, length, reference assignment, and controls verified for the selected interface.

## fal.ai MiniMax H3 Max

For H3 Max, I2V, T2V, R2V, Classic Control, Direct Explore, or Character Lock,
read [fal-h3-max.md](model-adapters/fal-h3-max.md). That adapter controls route
selection, reference order, seed optimization, prompt structure, and verified
fal.ai fields. It may translate packaging but cannot override GIGA identity,
approved continuity, or the selected style adapter.

When gameplay grounding is active, the provider prompt must preserve the selected build's geometry budget, texture/filtering/UV behavior, materials and lighting, effects density, draw distance, camera grammar, and capture characteristics. When a registered style adapter is active, preserve its rendering lock, temporal rhythm, expression preset, and motion profile instead. Avoid generic adapter language such as `cinematic lighting`, `volumetric`, `ultra-detailed`, `photoreal materials`, bokeh, or modern depth of field unless the selected build or adapter supports it.

## Image-generation adapter

Include:

1. identity reference assignment
2. adapter-specific character sheet assignment when active
3. subject construction and protected traits
4. current wardrobe/action/state
5. environment and spatial composition
6. selected adapter lock or grounded style observations
7. lighting, camera, and aspect ratio
8. decisive exclusions

When reference images are supported, assign each one a role. Do not tell a model to blend all references.

## Image-to-video adapter

Include:

1. approved start frame or storyboard as visual authority
2. duration and shot structure
3. one continuous action progression
4. character/object motion and contact points
5. camera movement per shot
6. continuity locks and end-state
7. selected motion profile, rhythm roles, and dominant motion channels
8. target style or game-engine motion/rendering behavior
9. negatives: no redesign, duplicates, extra limbs, unrequested text/dialogue/music, state resets

Keep appearance descriptions concise when the approved image already carries identity. Spend prompt budget on motion, geography, continuity, and preserving the selected style's period cadence.

## Seedance

Use storyboard/reference-first packaging when the current interface supports it. Write chronological shot beats with explicit transitions and a decisive final state. Carry `HOLD`, `BURST`, `INSERT`, and `REVEAL` rhythm roles as creative direction rather than assuming frame-exact timing. Keep camera direction dynamic but readable. Do not invent exact duration, aspect, audio, or reference-slot controls; verify the current interface or label them variable.

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
STYLE: selected adapter or observed era/build behavior
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
