import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cicd_demo.cli import main


class CliTests(unittest.TestCase):
    def test_greet_command(self):
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(["greet", "测试"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue().strip(), "你好，测试！CI/CD 运行成功。")

    def test_add_command(self):
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(["add", "1", "2", "3.5"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue().strip(), "6.5")


if __name__ == "__main__":
    unittest.main()
