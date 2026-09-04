# Animation Rules

Animate approved imagery. Do not redesign it.

## Preserve first

- GIGA identity, face geometry, hairline, beard, anatomy, proportions, and
  shoulder-to-waist silhouette
- current wardrobe, props, equipment, secondary identities, and damage
- environment, geography, shot composition, order, and screen direction
- palette, selected rendering style, light behavior, and aspect ratio
- spatial anchors and progressive action state

## Assign reference roles

Assign every reference one primary role: `IDENTITY`, `STYLE`, `PROJECT`, or
`MOTION`. List any intentional secondary role. A motion reference controls
timing, cuts, pose cadence, camera rhythm, or effects only; it does not override
identity, rendering, palette, environment, or audio.

Ignore source watermarks, captions, crop, letterboxing, interface elements, and
audio unless the user explicitly makes one authoritative.

## Motion grammar

Use the selected style adapter's motion rules when it defines them. Otherwise
use the active game's inspected animation behavior. For flagship PS2 this
normally means readable key poses, slightly rigid skeletal movement, limited
joint and finger articulation, simple cloth cycles, sparse era-appropriate
effects, and practical pans, cuts, tracks, or short push-ins.

Avoid modern motion capture, fluid cloth or muscle simulation, rubbery anatomy,
morphing facial geometry, hair/beard drift, duplicate subjects, extra limbs,
excessive motion blur, purposeless camera travel, or a held-image slideshow
when action is expected.

## Rhythm roles and motion budget

Tag every multi-shot beat:

- `HOLD`: tension, observation, strain, reflection, or reaction
- `BURST`: one decisive movement or action
- `INSERT`: an extremely brief hand, eye, prop, contact, or impact detail
- `REVEAL`: a readable new state or aftermath that deserves a hold

Storyboard panels do not imply equal duration. Principal shots may breathe;
inserts remain brief. Give each shot one dominant motion channel: `SUBJECT`,
`CAMERA`, or `EFFECTS`. Keep the other channels restrained. A held subject may
use one optical push-in or environmental effects, not both aggressively.

## State changes

For transformations, damage changes, wardrobe changes, or animated colorways,
record `PRE-STATE`, `CHANGE ONLY`, and `POST-STATE`. Preserve every unnamed
layer. Prefer a decisive transition between locked states instead of asking the
model to continuously reinterpret GIGA.

## Model-neutral multi-shot brief

```text
ANIMATION BRIEF

DURATION:
SHOT COUNT:
FORMAT:
SELECTED STYLE:
VISUAL AUTHORITY:
REFERENCE ROLES:
MOTION PROFILE:
STATE CHANGE:
AUDIO INTENT:

SHOT 1
RHYTHM ROLE:
DOMINANT MOTION:
CAMERA:
SUBJECT ACTION:
ENVIRONMENTAL MOTION:
SPATIAL STATE:
TRANSITION:

[repeat]

CONTINUITY:
PERIOD MOTION RULES:
ESSENTIAL NEGATIVES:
LOOP CONDITION:
```

Give each shot one main action and one dominant motion channel. When timing is
useful, make ranges total the requested runtime. Treat timecodes as direction
unless the selected host documents precise control.

## Model-neutral one-take brief

```text
MICRO-MOTION BRIEF

DURATION:
FORMAT:
SELECTED STYLE:
VISUAL AUTHORITY:
REFERENCE ROLES:
CONTINUOUS SUBJECT MOTION:
OPTIONAL SURFACE OR PALETTE MOTION:
OPTIONAL ENVIRONMENTAL MICRO-MOTION:
CAMERA RULE:
LOOP CONDITION:
CONTINUITY:
AUDIO INTENT:
ESSENTIAL NEGATIVES:
```

Use one continuous behavior instead of a timeline when motion is simple.

## Audio meaning

- `NO AUDIO` means generate no sound.
- `NO MUSIC` allows practical ambience and effects but no score or song.
- For separate voiceover, generate no speech and keep the approved script out
  of the video prompt.
- Do not promise speech or audio support unless the current interface confirms
  it.

## Prompt compression

Preserve in order:

1. identity, face, hair, beard, anatomy, and proportions
2. central action, continuity, and state-change delta
3. shot order, rhythm roles, and spatial progression
4. selected style construction and rendering
5. camera, motion profile, and period cadence
6. decisive negatives
7. secondary atmosphere

For an exact limit, remove explanation and duplication before protected layers,
count all characters including spaces and line breaks, and report the measured
count.
