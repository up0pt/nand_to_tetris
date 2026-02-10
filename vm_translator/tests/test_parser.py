import pytest
from parser import Parser
from pathlib import Path

class TestParser:
    def test_has_more_command(self, tmp_path: Path):
        p = tmp_path / "vmcmd.txt"
        p.write_text("push constant 0\npop local 0\npush argument 1\npop local 1", encoding="utf-8")

