import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cicd_demo.core import add, greet


class GreetTests(unittest.TestCase):
    def test_greet_returns_expected_message(self):
        self.assertEqual(greet("GitHub Actions"), "你好，GitHub Actions！CI/CD 运行成功。")

    def test_greet_trims_whitespace(self):
        self.assertEqual(greet("  开发者  "), "你好，开发者！CI/CD 运行成功。")

    def test_greet_rejects_empty_name(self):
        with self.assertRaisesRegex(ValueError, "名字不能为空"):
            greet("   ")


class AddTests(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add([1, 2, 3]), 6)

    def test_add_decimals(self):
        self.assertAlmostEqual(add([0.1, 0.2]), 0.3)

    def test_add_rejects_empty_input(self):
        with self.assertRaisesRegex(ValueError, "至少需要一个数字"):
            add([])


if __name__ == "__main__":
    unittest.main()
