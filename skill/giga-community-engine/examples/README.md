# Validation Matrix and Starter Requests

These text dry runs verify routing, authority, continuity, and output shape without incurring generation cost.

| Test | Starter request | Expected route and pass condition |
| --- | --- | --- |
| A — Canonical portrait | `Create a neutral PS2 character portrait of Gigachad.` | CHARACTER; uses bundled sheet, preserves face/hair/beard/physique, no generic bodybuilder drift |
| B — Training | `Gigachad practices precise heavy-bag combinations in an old boxing gym.` | TRAINING + SCENE; credible technique, disciplined tone, no automatic token copy |
| C — Everyday | `Gigachad waits alone at a laundromat at 2 a.m.` | STILL by default; identity survives an ordinary non-gym premise |
| D — Absurd meme | `Gigachad calmly audits a vending machine full of tiny dumbbells.` | MEME; one-glance deadpan premise, no clutter or unrequested captions |
| E — PS2 fidelity | `Original 2004 GTA San Andreas PS2-style Gigachad on a rural road.` | STILL/SCENE; first inspects authentic original-PS2 material, excludes remasters/mods, uses bundled PS2 model |
| F — Cinematic | `Gigachad repairs a storm-damaged radio tower in 6 shots.` | CLASSIC CINEMATIC; genesis approval, 5-7 distinct shots, coherent geography and action |
| G — Commercial | `A fictional PS2 commercial for GIGA Moving Company.` | COMMERCIAL; immediate visual hook, serious in-world treatment, clear payoff/end card, no financial claim |
| H — Episode | `Gigachad enters a dead mall where the mannequins move when unseen.` | EPISODE; four progressive approved boards: Hook + Setup, Escalation, Turn, Payoff; Board 5 only if justified |
| I — Crossover | `Gigachad and a small pink-durag Chihuahua train together.` | Separate identity blocks; no face, beard, physique, wardrobe, or anatomy contamination |

## Repair checks

Run after any test:

- `Approved.` advances and preserves the current authority.
- `The face drifted. Fix only the face.` invokes a narrow repair, not a redesign.
- `Shot 4 reverses direction.` repairs orientation while locking identity, world, and other shots.
- `Use Seedance 2.0, PS2 dynamic camera, under 3500 characters.` produces a measured provider prompt without inventing controls.

## Textual dry-run result

The v1 route audit passes all nine cases at the instruction level:

- every request maps to one primary mode
- PS2 identity resolves to the bundled approved sheet
- named-game requests trigger fresh screenshot grounding
- cinematic and episode gates preserve approvals and progressive state
- secondary identities remain isolated
- commercial and community outputs retain rights and financial guardrails
- provider adaptation occurs after the model-neutral brief

Rendered likeness remains a generation-time check. Repair against the latest approved image when a model fails.
