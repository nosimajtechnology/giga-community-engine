# Late-Z Battle Cel Adapter v1.2

## Purpose and activation

Adapter ID: `late-z-battle-cel-v1`

Adapter version: `1.2`

Display signifier: `LATE-Z BATTLE CEL`

Use for GIGA images and cinematics that request Late-Z Battle Cel,
Buu-saga-inspired, mid-1990s DBZ-esque battle anime, or an approved project
image in that treatment. This is a render-and-motion adapter. It replaces the
flagship PS2 build while active; do not mix cel animation with 3D game
rendering unless the user explicitly requests a hybrid.

Borrow period visual grammar only. Do not add franchise characters, costumes,
symbols, attacks, locations, logos, or story canon unless the user separately
requests them.

## Reference assignments

- `../../assets/giga-character-sheet.png` remains the canonical authority for
  GIGA's long angular face, heavy brow, deep-set narrow eyes, nose, squared
  jaw, slicked-back dark hair, shaped connected beard, coherent muscular
  anatomy, shoulder-to-waist ratio, long legs, and recognizable silhouette.
- `../../assets/style-adapters/late-z-battle-cel/giga-late-z-character-sheet-v1.png`
  is the bundled Late-Z translation authority for neutral front,
  three-quarter, profile, rear, and close-up construction; warm tan cel
  palette; hair and beard treatment; line economy; anatomy simplification;
  black-trouser wardrobe; and sheet-local surface treatment. Its SHA-256 is
  `b87ef34a8a2e4ef08a09e81d63b0c61899101197d40aeef44aa4c287ddc16eea`.
- A user-approved project image controls current rendering, wardrobe,
  environment, lighting, pose, and continuity.
- Target-era cel references control line, paint, camera, and motion grammar
  only. They may not import protected character or franchise content.

When image tooling accepts references, assign the canonical sheet to
underlying identity and construction, and the bundled Late-Z sheet to the
adapter-specific visual translation. Assign any approved project image to
current continuity. The adapter sheet never replaces the canonical identity.

Exception for H3 Max R2V: upload only the bundled Late-Z GIGA sheet as `Image
1` by default. For that route, it is the consolidated authority for identity,
face, anatomy, costume, proportions, palette, linework, cel shading, and
broadcast rendering. Do not also attach the canonical sheet or raw broadcast
captures unless the user requests them, the scene needs another narrow
authority, or a failed result needs a targeted repair.

## Reference-role firewall

Assign every supplied reference a primary role before generation:

- **IDENTITY:** canonical GIGA sheet or approved project GIGA
- **STYLE:** bundled Late-Z character sheet, approved project image, or
  target-era cel reference
- **PROJECT:** approved frame or storyboard controlling current continuity
- **MOTION:** clips controlling only timing, cuts, camera rhythm, pose cadence,
  or effects behavior

A mixed-era or off-target motion clip may guide cadence without becoming style
authority. Do not inherit its characters, anatomy, palette, aura colors,
locations, logos, crop, letterboxing, watermark, captions, or audio. Reference
audio is non-authoritative unless the user explicitly assigns it an audio role.

## Rendering lock

- original 4:3 mid-1990s television-cel presentation
- confident dark brown-black ink contours, thicker on the outer silhouette and
  thinner on sparse facial, beard, and anatomy marks
- clean simplified forms with two opaque cel values and an occasional third
  highlight; hard-edged shadow shapes and no soft character gradients
- warm tan skin translated into ochre-tan base, muted umber shadow planes, and
  restrained pale highlights
- slicked-back hair and shaped connected beard rendered as stable dark paint
  masses with economical strand marks; never fluffy, spiked, or individually
  simulated
- muscular anatomy remains extreme but coherent: broad square shoulders,
  thick neck, powerful chest/back/arms, narrow waist, and long legs without
  parody inflation
- default loose straight black trousers and black shoes use simple charcoal
  shadow planes when that wardrobe is active
- hand-painted backgrounds use broad opaque shapes, sparse terrain marks, and
  atmospheric color recession rather than dense digital detail
- very light fine analog cel-photography grain, restrained broadcast softness,
  and minute color bleed; no obvious aging effect
- in animation, grain remains a stable finishing texture rather than crawling,
  boiling, or redrawing independently

## GIGA identity translation

Preserve the specific recognizable adult male rather than a generic handsome
bodybuilder: long angular face, heavy brow, deep-set narrow eyes, strong cheek
structure, long straight-to-angular nose, broad squared jaw, controlled
slicked-back hairline, full shaped beard connected to the moustache, stoic
expression, warm tan skin, thick neck, broad shoulders, narrow waist, and long
powerful limbs.

The style may simplify surfaces, but it may not shorten or round the face,
widen the eyes, replace the nose, add a fringe or widow's-peak redesign,
lengthen or remove the beard, compress the legs, or turn the physique into a
superhero caricature. Clothes must fit the same body instead of replacing it.

## Expression preset: BATTLE_INTENSE

Use only for intense confrontation or when requested. Change expression, not
identity:

- lower the upper eyelids slightly over the existing deep-set narrow eyes
- tighten the heavy brow and add one or two short tension creases
- keep the jaw set and mouth closed or minimally parted
- preserve the exact nose, cheek planes, face length, hairline, beard outline,
  age, and head-to-body ratio

Do not add bright battle irises, giant white sclera, gritted oversized teeth,
spiked hair, or a permanent angry redesign. The normal preset remains stoic
and controlled.

## Camera and composition

Favor original-TV-anime framing: tense close-ups and medium close-ups for
decision or strain; low three-quarter views and restrained dutch angles for
confrontation; wide aftermath frames that hold the body against painted
terrain; strong asymmetry, foreground rocks or debris, and clear silhouettes;
practical pans, short push-ins, snap reframes, and decisive cuts.

Create dynamism through contrast between compositions: wide establish, tight
strain close-up, extreme detail insert, release, reaction, and aftermath. Do
not solve a static sequence with constant camera movement.

Keep 4:3 unless the user explicitly requests another delivery format. Avoid
modern shallow depth of field, glossy lens effects, floating drone movement,
or continuous orbiting.

## Temporal rhythm

For animated work:

- use held key poses with limited secondary motion, then brief decisive bursts
- let principal shots breathe; do not assign every storyboard panel equal time
- tag each beat `HOLD`, `BURST`, `INSERT`, or `REVEAL`
- use visibly stepped pose changes and repeated drawings instead of perfectly
  smooth interpolation; effects may update faster than the character
- give each shot one dominant motion channel: subject, camera, or effects
- during a hold, allow restrained environmental motion or one short optical
  push-in, not both aggressively
- favor hard cuts and use a very brief impact cel only when contact or a state
  change needs punctuation
- keep face, hairline, beard edge, body contours, cel shadows, and grain stable;
  no line boil, anatomy drift, elastic zoom, or wardrobe crawling

## Motion profiles

### POWER_UP_TRANSFORM

Build from discrete states: intact pre-state; held strain pose with escalating
weather, dust, debris, aura pressure, or environmental response; progressively
tighter hard cuts or one restrained push-in; one brief silhouette/impact
insert; hard cut to the completed post-state; held reveal and reaction or
aftermath.

Record:

```text
PRE-STATE:
CHANGE ONLY:
POST-STATE:
```

The delta controls only named changes. Preserve face geometry, hairline,
beard, anatomy, proportions, wardrobe construction, position, and environment
unless named. Never continuously morph the face, body, hair, or clothes between
states.

### IMPACT_MELEE

Use a readable chain: launch or approach, one strike, very brief contact
insert, follow-through, opponent reaction, aftermath. Use one attack path per
principal shot. Do not ask for an extended exchange, simultaneous attacks, or
prolonged overlapping limbs. Keep exactly one head, one torso, two arms, and
two legs per character.

For 8-15 seconds, prefer four or five principal shots plus no more than two
brief inserts. Written durations guide rhythm rather than guaranteeing
frame-accurate control.

### TRAINING_BURST

Use a compact training rhythm: held ready pose, one explosive clean rep or
technique, brief detail insert at peak effort, controlled recovery, and a
quiet aftermath hold. Keep equipment contact and body mechanics readable.
Superhuman speed may compress the action, but it may not multiply limbs,
weights, or equipment.

## Exclusions

- no glossy modern digital-anime finish, remaster coloring, airbrushed
  gradients, volumetric light, lens flare, or cinematic depth of field
- no 3D, CGI, PS2 render, photoreal skin, modern subsurface materials, or
  plastic toy rendering
- no heavy grain, VHS noise, scanlines, scratches, film burns, chromatic
  aberration, sepia cast, vignette, CRT border, or compression blocks
- no generic bodybuilder face, superhero redesign, parody muscle inflation,
  altered hairline, missing beard, spiked transformation hair, franchise
  traits, logos, subtitles, HUD, or watermark by default
- no constant camera motion, equal-duration montage rhythm, smooth
  transformation morph, crawling grain, line boil, or fluid modern
  interpolation

## Repair checks

- **too clean:** add only very light fine cel-photography grain and restrained
  broadcast softness
- **too painterly:** remove soft blends and excess anatomy hatching; restore
  opaque planes, hard shadows, and economical interior lines
- **identity drifts:** restore the long angular face, heavy brow, narrow eyes,
  nose, squared jaw, controlled slicked-back hairline, shaped connected beard,
  coherent physique, long legs, and shoulder-to-waist silhouette
- **generic anime bodybuilder:** restore the canonical craniofacial geometry
  before decorative style; simplify background or camera before relaxing
  identity
- **camera feels stiff:** add shot-scale contrast, one restrained push-in, or a
  decisive cut; never constant orbiting or random handheld movement
- **transformation morphs:** restore locked pre- and post-states and bridge them
  only with effects plus one brief impact insert
- **held drawing crawls:** stabilize face, hair, beard, body contours, cel
  shadows, and grain; animate only the declared dominant motion channel
- **melee duplicates anatomy:** reduce to one readable strike and attack path;
  restore exact limb counts before adding effects
