#!/usr/bin/env python3
"""Deterministic policy checks for reference-grounded gameplay fidelity."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skill" / "giga-community-engine"


def read(relative: str) -> str:
    return (SKILL / relative).read_text(encoding="utf-8")


class ReferenceGroundingPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.entry = read("SKILL.md")
        cls.grounding = read("references/rendering-grounding.md")
        cls.modes = read("references/modes.md")
        cls.continuity = read("references/continuity.md")
        cls.adapters = read("references/model-adapters.md")
        cls.transformations = read("references/transformations.md")
        fixture_path = ROOT / "tests" / "fixtures" / "reference_grounding.json"
        cls.fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))

    def test_all_selection_sources_route_to_grounding(self) -> None:
        for source in ("user", "inherited", "agent", "mode default"):
            self.assertIn(source, self.grounding)
        self.assertIn("rendering-grounding.md", self.entry)
        self.assertIn("selected by the Engine", self.transformations)

    def test_source_quality_and_rejections_are_operational(self) -> None:
        for requirement in (
            "three to five useful screenshots",
            "original-platform gameplay captures",
            "remasters",
            "emulator texture packs",
            "mods",
            "platform cannot be reasonably identified",
            "Inspect the images themselves",
            "Do not commit or redistribute third-party screenshots",
        ):
            self.assertIn(requirement, self.grounding)

    def test_rendering_contract_is_complete(self) -> None:
        for field in (
            "SOURCE QUALITY",
            "REFERENCE ROLES",
            "OBSERVED GEOMETRY",
            "OBSERVED TEXTURES / FILTERING / UV",
            "OBSERVED MATERIALS / LIGHTING / SHADOWS",
            "OBSERVED ENVIRONMENT / EFFECTS / DRAW DISTANCE",
            "OBSERVED CAMERA / SUBJECT SCALE / ANIMATION",
            "CAPTURE CHARACTERISTICS",
            "DECISIVE EXCLUSIONS",
            "IDENTITY PRESERVATION",
        ):
            self.assertIn(field, self.grounding)

    def test_gate_and_single_repair_stopping_rule(self) -> None:
        self.assertIn("One major identity failure fails", self.grounding)
        self.assertIn("Two or more era-fidelity failures fail", self.grounding)
        self.assertIn("one automatic narrow repair", self.grounding)
        self.assertIn("if the second attempt fails", self.grounding)
        self.assertIn("Do not show or expand a frame that fails", self.modes)

    def test_relevant_modes_use_grounded_prefix(self) -> None:
        prefix = self.modes.split("## CHARACTER", 1)[0]
        for mode in ("STILL", "SCENE", "CLASSIC CINEMATIC", "TRAINING", "COMMERCIAL", "EPISODE"):
            self.assertIn(mode, prefix)

    def test_continuity_and_adapter_preserve_contract(self) -> None:
        self.assertIn("screenshot-reference set", self.continuity)
        self.assertIn("rendering contract", self.continuity)
        self.assertIn("sharper, denser, more cinematic, or more modern", self.continuity)
        self.assertIn("SCREENSHOT-DERIVED RENDERING CONTRACT", self.adapters)
        for unsafe_default in ("cinematic lighting", "volumetric", "ultra-detailed", "photoreal materials"):
            self.assertIn(f"`{unsafe_default}`", self.adapters)

    def test_non_game_requests_are_explicitly_excluded(self) -> None:
        self.assertIn("modern studio portrait", self.grounding)
        self.assertIn("explicit non-game build", self.grounding)

    def test_fixtures_cover_a_through_h(self) -> None:
        self.assertEqual([fixture["id"] for fixture in self.fixtures], list("ABCDEFGH"))
        self.assertFalse(next(item for item in self.fixtures if item["id"] == "F")["grounding"])
        self.assertEqual(next(item for item in self.fixtures if item["id"] == "B")["selection_source"], "agent")
        self.assertEqual(next(item for item in self.fixtures if item["id"] == "G")["selection_source"], "inherited")
        for fixture in self.fixtures:
            self.assertTrue(fixture["prompt"])
            self.assertTrue(fixture["invariants"])


if __name__ == "__main__":
    unittest.main()
