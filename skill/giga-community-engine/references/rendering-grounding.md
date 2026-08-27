# Reference-Grounded Gameplay Fidelity

Use this workflow whenever an era-specific game build is active. Gameplay fidelity comes from inspected original-build images, not retro keywords or post-applied filters.

## Resolve the active build

Resolve once, in this order:

1. **User** — explicit game, console, platform, generation, year, realism level, or modern-rendering instruction
2. **Inherited** — latest approved frame or storyboard in the current project
3. **Agent** — a deliberate Engine choice that best serves the concept
4. **Mode default** — an existing relevant default that does not conflict with the request

Record internally:

```text
ERA SELECTION SOURCE: user | inherited | agent | mode default
TARGET BUILD: game / platform / year or console generation
GROUNDING REQUIRED: yes | no
```

Do not ask the user to choose when the concept can be routed confidently. State an Engine-selected build briefly only when it materially affects the result.

## Trigger rules

Ground before generation when the active build specifies:

- PS1/PlayStation, Nintendo 64, Saturn, fifth generation, or an equivalent build
- PS2, Dreamcast, GameCube, original Xbox, sixth generation, or an equivalent build
- PS3, Xbox 360, seventh generation, or an equivalent build
- a named game's fidelity or gameplay-camera language
- a gameplay screenshot, in-game-rendered scene, real-time game trailer, or equivalent era-specific output
- an era intentionally selected by the Engine

Do not trigger merely because the subject is GIGA, a scene is nostalgic, a mode is cinematic, or the bundled PS2 identity sheet exists. A modern studio portrait, photographic request, style-neutral character study, or explicit non-game build follows its normal route.

## Research authentic captures

Before the first or genesis frame, retrieve and visually inspect three to five useful screenshots when available:

1. action and gameplay-camera reference
2. environment and architecture reference
3. geometry, texture, material, and lighting reference
4. optional NPC, enemy, vehicle, machinery, or equipment reference
5. optional exact named-game/platform reference

Prefer identifiable original-platform gameplay captures, then original-platform in-engine cutscenes, then contemporary reviews, manuals, official archives, or reliable screenshot databases that clearly identify the game, platform, and release. Use a secondary source only when the build can still be reasonably verified.

Reject remasters, remakes, HD collections, later ports, backward-compatible enhancements, emulator texture packs, widescreen hacks, fan patches, ReShade, mods, promotional art, box art, pre-rendered cinematics, fan renders, modern concept art, and captures whose platform cannot be reasonably identified. Inspect the images themselves; titles and prose are not visual inspection.

Do not commit or redistribute third-party screenshots in the public package.

## Assign narrow reference roles

Use equivalent assignments before generation:

```text
GIGA IDENTITY AUTHORITY — approved canonical reference or bundled PS2 turnaround;
face, hair, beard, physique, proportions, and silhouette only.

APPROVED PROJECT AUTHORITY — wardrobe, props, environment, geography, lighting,
palette, damage, and action state.

GAMEPLAY REFERENCE A — action camera, subject scale, and spacing only.
GAMEPLAY REFERENCE B — environment massing, asset density, and draw distance only.
GAMEPLAY REFERENCE C — geometry, textures, materials, lighting, shadows, and effects only.

SECONDARY CHARACTER AUTHORITY — one isolated identity block per character.
USER MOOD REFERENCE — mood or composition only unless explicitly reassigned.
```

Never tell a model to blend every reference. Rendering references are lower authorities and cannot overwrite GIGA, a secondary identity, an approved outfit, or current scene state.

## Derive the rendering contract

Write a compact internal contract before prompting:

```text
ERA SELECTION SOURCE: [...]
TARGET BUILD: [game / platform / year or console generation]
SOURCE QUALITY: [why the inspected captures are credible]
REFERENCE ROLES: [...]
OBSERVED GEOMETRY: [...]
OBSERVED TEXTURES / FILTERING / UV: [...]
OBSERVED MATERIALS / LIGHTING / SHADOWS: [...]
OBSERVED ENVIRONMENT / EFFECTS / DRAW DISTANCE: [...]
OBSERVED CAMERA / SUBJECT SCALE / ANIMATION: [...]
CAPTURE CHARACTERISTICS: [aspect, resolution feel, aliasing, post-processing]
DECISIVE EXCLUSIONS: [wrong era, remasters, mods, modern cues]
IDENTITY PRESERVATION: [face, hair, beard, physique, silhouette]
```

Use the PS1, PS2, and PS3 notes in [transformations.md](transformations.md) as baselines, then refine them from the inspected build. Do not mechanically reuse one PS2 contract for GTA San Andreas, Shinobi, Def Jam, Tekken, sports games, or other visually distinct titles.

Named-game grounding transfers general rendering, environment-density, and camera behavior only. Do not copy protected characters, faces, costumes, HUDs, logos, exact levels, signature props, moves, or shot compositions.

## Required grounded workflow

For an active triggered build, STILL, SCENE, CLASSIC CINEMATIC, image-based TRAINING, COMMERCIAL, and EPISODE use:

```text
IDEA -> ACTIVE BUILD -> SCREENSHOT SEARCH -> VISUAL INSPECTION
-> REFERENCE ROLES -> RENDERING CONTRACT -> FIRST / GENESIS FRAME
-> IDENTITY + FIDELITY GATE -> USER APPROVAL -> NEXT OUTPUT
```

Keep the approved identity model, environment build, geometry budget, texture density, material and lighting model, effects density, draw distance, camera grammar, and capture characteristics in every connected panel, board, and animation prompt.

## Identity + fidelity gate

Inspect a grounded generated frame before showing it.

One major identity failure fails the gate:

- generic bodybuilder or unrelated handsome face
- wrong jaw, brow, nose, hair, beard, physique, or shoulder-to-waist silhouette
- contamination from a game character or secondary subject
- anatomy or realism that conflicts with the active GIGA model

Two or more era-fidelity failures fail the gate:

- materials, skin, hair, cloth, or equipment look substantially newer than the target
- geometry or environment density exceeds the inspected build
- debris, particles, crowds, vegetation, or effects exceed reference density
- later-generation volumetrics, global illumination, bokeh, or depth of field appear without support
- camera reads as modern concept art or photography instead of gameplay/in-engine footage
- softness, noise, scanlines, or grading merely cover modern assets
- the result belongs to a different console generation

On failure:

1. do not present the frame as an approval candidate
2. lock all correct identity, action, composition, geography, and scene layers
3. apply one automatic narrow repair when isolated
4. regenerate from scratch when identity and rendering construction both fail
5. run the gate again
6. if the second attempt fails, state the limitation briefly and ask whether to try another grounded generation

Do not make the user diagnose generic identity drift or modern-rendering drift on the first attempt.
