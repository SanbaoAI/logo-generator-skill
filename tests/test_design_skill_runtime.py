import json
import unittest
from pathlib import Path

from core.prompt_compiler import PromptContext, build_prompt
from core.runtime import DesignSkillRuntime
from skills.skill_router import route


ROOT = Path(__file__).resolve().parents[1]


class DesignSkillRuntimeTest(unittest.TestCase):
    def setUp(self):
        self.memory = json.loads((ROOT / "memory" / "brand_default.json").read_text())

    def test_router_selects_social_media_for_xiaohongshu(self):
        self.assertEqual(route("帮我做一个AI工具发布的小红书宣传图"), "social_media_skill")

    def test_router_selects_corporate_website_for_official_site(self):
        self.assertEqual(route("帮我做一个企业品牌名片型官网"), "corporate_website_skill")

    def test_prompt_compiler_preserves_structured_context(self):
        prompt = build_prompt(
            PromptContext(
                brand_memory={"brand_id": "demo"},
                last_design={"asset_id": "logo_v1"},
                scene={"platform": "xiaohongshu"},
                task={"request": "social launch"},
            )
        )

        self.assertEqual(prompt["brand_memory"]["brand_id"], "demo")
        self.assertEqual(prompt["last_design"]["asset_id"], "logo_v1")
        self.assertEqual(prompt["scene"]["platform"], "xiaohongshu")
        self.assertEqual(prompt["task"]["request"], "social launch")

    def test_social_media_runtime_outputs_publishable_five_slide_carousel(self):
        result = DesignSkillRuntime().run(
            "帮我做一个AI工具发布的小红书宣传图",
            input_data={
                "platform": "xiaohongshu",
                "product": "AI design tool",
                "cta": "立即试用",
            },
            memory=self.memory,
        )

        output = result["output"]
        self.assertEqual(result["skill"], "social_media_skill")
        self.assertEqual(output["platform"], "xiaohongshu")
        self.assertEqual(output["layout"]["slides"], 5)
        self.assertEqual(output["layout"]["structure"], ["hook", "problem", "solution", "product", "cta"])
        self.assertTrue(output["final_output"]["publish_ready"])
        self.assertEqual(output["styled_plan"]["colors"]["primary"], self.memory["visual_dna"]["primary_color"])
        self.assertGreaterEqual(result["critique"]["brand_consistency"], 0.85)
        self.assertEqual(result["memory"]["history"][-1]["type"], "social_media_carousel")

    def test_corporate_website_runtime_outputs_role_based_directory_plan(self):
        result = DesignSkillRuntime().run(
            "帮我做一个企业品牌名片型官网",
            input_data={
                "company_name": "Sanbao Design AI",
                "industry": "AI brand design",
                "business": "enterprise brand identity and website generation",
                "target_users": "founders and product teams",
                "core_value": "a clear official website and reusable brand system",
                "brand_tone": "professional, modern, design-led",
            },
            memory=self.memory,
        )

        output = result["output"]
        self.assertEqual(result["skill"], "corporate_website_skill")
        self.assertEqual(output["type"], "corporate_website_brand_card")
        self.assertIn("product_manager", output["roles"])
        self.assertIn("content_copy_validator", output["roles"])
        self.assertIn("content_validation", output)
        self.assertIn("design_director", output["roles"])
        self.assertIn("brand_design", output)
        self.assertIn("color_design", output)
        self.assertIn("typography_designer", output["roles"])
        self.assertIn("typography_design", output)
        self.assertIn("japanese_typography_consultant", output["roles"])
        self.assertIn("typography_consultant", output)
        self.assertIn("visual_assets", output)
        self.assertIn("ui_design", output)
        self.assertTrue(output["final_output"]["directory_separated"])
        self.assertTrue(
            any(path.endswith("08-visual-assets/icons/") for path in output["output_directories"]["directories"])
        )
        self.assertTrue(
            any(path.endswith("06-typography-system/") for path in output["output_directories"]["directories"])
        )
        self.assertTrue(
            any(path.endswith("07-typography-consultant/") for path in output["output_directories"]["directories"])
        )
        self.assertTrue(
            any(path.endswith("02-content-validation/") for path in output["output_directories"]["directories"])
        )
        self.assertEqual(output["layout"]["sections"], len(output["layout"]["structure"]))
        self.assertGreaterEqual(result["critique"]["clarity"], 0.85)
        self.assertEqual(result["memory"]["history"][-1]["type"], "corporate_website_brand_card")


if __name__ == "__main__":
    unittest.main()
