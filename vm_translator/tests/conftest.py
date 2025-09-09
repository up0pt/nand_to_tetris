from pathlib import Path
import pytest

from vm_translator.code_writer import CodeWriter


@pytest.fixture
def output_path(tmp_path: Path) -> Path:
    return tmp_path / "out.asm"


@pytest.fixture
def cw(output_path: Path) -> CodeWriter:
    return CodeWriter(output_path)
