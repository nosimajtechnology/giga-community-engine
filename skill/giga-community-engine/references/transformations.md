# Transformation System

Preserve identity geometry and silhouette while changing rendering technology. A style label never authorizes face redesign.

Registered visual adapters route through
[style-adapters.md](style-adapters.md). When `late-z-battle-cel-v1` is active,
read its adapter reference instead of treating cel anime as a loose
transformation. This file continues to control named game generations,
photographic work, generic low-poly work, meme grammar, and other unregistered
transformations.

## Ground before generating

When an era-specific game build is active—whether user-selected, inherited, selected by the Engine, or supplied by a mode default—read and follow [rendering-grounding.md](rendering-grounding.md) before generation.

The construction notes below are reusable baselines, not substitutes for inspected screenshots. Refine them from the requested original game/platform build. When grounding is active:

1. search for authentic material from the requested version, platform, and era
2. visually inspect representative gameplay and in-engine cutscene screenshots
3. record observed polygon density, texture resolution, lighting, fog, materials, camera, animation, environment density, and UI behavior
4. separate platform facts from later remasters, mods, fan renders, and promotional art
5. translate those observations into the scene while keeping GIGA identity under the higher authority

Use the smallest useful reference set with narrow roles rather than a collage of loosely related material. If exact fidelity cannot be verified, call the result `inspired by`, not authentic.

## Photographic / realistic

- prioritize approved likeness and believable anatomy
- use controlled, sculptural lighting without copying a protected photograph's exact composition
- retain the specific jaw, hair, beard, brow, nose, and silhouette
- avoid waxy skin, beauty-model drift, over-sharpened pores, or superhero-costume defaults

## PS1 / fifth generation

- very low polygon count with blocky joints and simplified hands
- face identity carried by head silhouette, brow/nose/jaw planes, painted beard and hair masses
- 32-128 px-looking texture density, affine texture wobble, vertex jitter, banded color, hard aliasing, limited draw distance
- simple baked or vertex lighting; no modern PBR, ray tracing, dense hair cards, or cinematic depth of field
- use close-ups sparingly because the face has limited geometry; recognizable silhouette must do more work

## PS2 / sixth generation

Use the bundled turnaround as direct authority.

- low-to-moderate polygon human model, readable planar anatomy, simple fingers
- low-resolution painted skin, beard, and hair textures
- Gouraud/vertex-style shading, baked light, restrained specular response, modest shadowing
- jagged edges, limited material complexity, compressed texture feel, era-correct environment density
- keep the warm/tan skin, slicked-back dark hair, shaped beard, black-trouser default, and approved proportions unless changed by the project
- do not polish into current-gen CGI or collapse into PS1 blocks

## PS3 / Xbox 360 / seventh generation

- higher-poly but still clearly in-engine character, stronger normal maps, harder specular highlights, sharper textures, heavier post-processing
- era-typical bloom, contrast, screen-space effects, and sometimes desaturated or color-graded presentation
- hair remains sculpted/mesh-like rather than strand-perfect; skin may show texture but not modern scan-level realism
- preserve the same craniofacial construction and shoulder-to-waist silhouette
- avoid current-gen subsurface skin, path-traced lighting, micro-groomed facial hair, and ultra-clean 4K materials

## Generic low-poly

Specify the intended generation. `Low-poly` alone is not a complete style. Favor readable planes and silhouette over arbitrary faceting. Do not use a toy-like or cute proportion system unless requested.

## Retro commercial

- treat the fictional product or service seriously inside the world
- use era-correct product staging, logo-object simplicity, camera movement, typography only when text is truly needed, and a decisive end-card beat
- lead with visual failure, need, product, transformation, or absurd hook rather than slow exposition
- separate exact narration into a voiceover route when a video model cannot reliably deliver it

## Meme image

- make the idea legible in one glance
- use identity, contrast, situation, or reaction before adding text
- preserve space for user-added text when exact typography matters
- avoid stacking token logos, charts, captions, and visual gags until the premise becomes unreadable

## Cinematic

- preserve game-engine constraints across every shot
- use distinct shot purposes and dynamic perspectives where appropriate
- favor one readable action progression over unrelated spectacle
- keep the impossible premise sincere; do not add winks, fourth-wall reactions, or dialogue unless requested

## Fidelity prompt block

Record observations before prompting:

```text
TARGET BUILD: [game / platform / year or console generation]
OBSERVED GEOMETRY: [...]
OBSERVED TEXTURES/MATERIALS: [...]
OBSERVED LIGHTING/ATMOSPHERE: [...]
OBSERVED CAMERA/ANIMATION: [...]
EXCLUSIONS: [remasters, mods, modern rendering cues]
IDENTITY PRESERVATION: [face/hair/beard/physique/silhouette]
```
