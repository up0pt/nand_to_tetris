from collections.abc import Callable
from pathlib import Path
from textwrap import dedent

import pytest

from compilation_engine import CompilationEngine

@pytest.fixture
def make_compilation_engine(tmp_path: Path) -> Callable[[str], tuple[CompilationEngine, Path]]:
    def make(input_text: str) -> tuple[CompilationEngine, Path]:
        input_path = tmp_path / "Main.jack"
        output_path = tmp_path / "Main.xml"
        input_path.write_text(
            input_text,
            encoding="utf-8"
        )
        return CompilationEngine(input_path, output_path), output_path

    return make

@pytest.mark.parametrize(
        ("text", "expected"),
        [
            (
                "  \n class  abc\n\n {}", 
                dedent("""\
                    <class>
                        <keyword> class </keyword>
                        <identifier> abc </identifier>
                        <symbol> { </symbol>
                        <symbol> } </symbol>
                    </class>"""))
        ]
)
def test_compile_class_plain_all(text: str, expected: str, make_compilation_engine: Callable[[str], tuple[CompilationEngine, Path]]):
    compilation_engine, output_path = make_compilation_engine(text)
    compilation_engine.compile_class()
    assert output_path.read_text("utf-8") == expected