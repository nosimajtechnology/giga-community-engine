# Changelog

## [1.3.0] - 2026-09-04

### Added

- Late-Z Battle Cel style adapter and bundled GIGA translation sheet.
- H3 Max Classic Control (I2V), Direct Explore (T2V), and Character Lock (R2V)
  routes with explicit reference-role ordering.
- Seed optimization, verified fal.ai fields, model-aware staging, and
  route-specific repair guidance.

### Preserved

- The classic Genesis Frame → storyboard workflow, with the approved storyboard
  translated into the chronological H3 Max prompt rather than uploaded by default.

## [1.1.0] - 2026-08-27

### Added

- Reference-grounded gameplay fidelity for user-selected, inherited, Engine-selected, and mode-default game eras.
- Original-platform screenshot source checks, narrow reference roles, and a screenshot-derived rendering contract.
- A pre-presentation GIGA identity and era-fidelity gate with one automatic narrow repair when appropriate.
- Maintained PS1, PS2, PS3, named-game, non-trigger, continuity, and secondary-character regression fixtures.

### Changed

- Grounded STILL, SCENE, CLASSIC CINEMATIC, image-based TRAINING, COMMERCIAL, and EPISODE workflows now lock the approved rendering contract through storyboards and animation prompts.
- Provider adapters now prevent generic modern cinematic language from overriding an older-console build.

### Preserved

- Beginner installation, modes, approvals, episode architecture, GIGA identity authority, cultural boundaries, and the permanent latest-download URL.
