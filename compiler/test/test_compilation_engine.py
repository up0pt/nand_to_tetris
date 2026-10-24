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

@pytest.mark.parametrize(
        ("text", "expected"),
        [
            (
                "  \n class  abc\n\n {static int num_1,\n\n num_2,   flag \n;\n field classname Class2, class_34;}", 
                dedent("""\
                    <class>
                    <keyword> class </keyword>
                    <identifier> abc </identifier>
                    <symbol> { </symbol>
                    <classVarDec>
                    <keyword> static </keyword>
                    <keyword> int </keyword>
                    <identifier> num_1 </identifier>
                    <symbol> , </symbol>
                    <identifier> num_2 </identifier>
                    <symbol> , </symbol>
                    <identifier> flag </identifier>
                    <symbol> ; </symbol>
                    </classVarDec>
                    <classVarDec>
                    <keyword> field </keyword>
                    <identifier> classname </identifier>
                    <identifier> Class2 </identifier>
                    <symbol> , </symbol>
                    <identifier> class_34 </identifier>
                    <symbol> ; </symbol>
                    </classVarDec>
                    <symbol> } </symbol>
                    </class>"""))
        ]
)
def test_compile_class_class_var_dec(text: str, expected: str, make_compilation_engine: Callable[[str], tuple[CompilationEngine, Path]]):
    compilation_engine, output_path = make_compilation_engine(text)
    compilation_engine.compile_class()
    assert output_path.read_text("utf-8") == expected

@pytest.mark.parametrize(
        ("text", "expected"),
        [
            (
                """
                class abc {
                    static int num_1, num_2, flag;
                    field classname Class2, class_34;
                
                    constructor void make_new_hello (int num1, class_32 new_one) {
                    var int ans, boolean flag2;
                }
                
                }""", 
                dedent("""\
                    <class>
                    <keyword> class </keyword>
                    <identifier> abc </identifier>
                    <symbol> { </symbol>
                    <classVarDec>
                    <keyword> static </keyword>
                    <keyword> int </keyword>
                    <identifier> num_1 </identifier>
                    <symbol> , </symbol>
                    <identifier> num_2 </identifier>
                    <symbol> , </symbol>
                    <identifier> flag </identifier>
                    <symbol> ; </symbol>
                    </classVarDec>
                    <classVarDec>
                    <keyword> field </keyword>
                    <identifier> classname </identifier>
                    <identifier> Class2 </identifier>
                    <symbol> , </symbol>
                    <identifier> class_34 </identifier>
                    <symbol> ; </symbol>
                    </classVarDec>
                    <subroutineDec>
                    <keyword> constructor </keyword>
                    <keyword> void </keyword>
                    <identifier> make_new_hello </identifier>
                    <symbol> ( </symbol>
                    <parameterList>
                    <keyword> int </keyword>
                    <identifier> num1 </identifier>
                    <symbol> , </symbol>
                    <identifier> class_32 </identifier>
                    <identifier> new_one </identifier>
                    </parameterList>
                    <symbol> ) </symbol>
                    <subroutineBody>
                    <symbol> { <symbol>
                    <varDec>
                    <keyword> var </keyword>
                    <keyword> int </keyword>
                    <identifier> ans </identifier>
                    <symbol> , </symbol>
                    <keyword> boolean </keyword>
                    <identifier> flag2 </identifier>
                    <symbol> ; </symbol>
                    </varDec>
                    </subroutineBody>
                    </subroutineDec>
                    <symbol> } </symbol>
                    </class>"""))
        ]
)
def test_compile_subroutine_dec_wo_statement(text: str, expected: str, make_compilation_engine: Callable[[str], tuple[CompilationEngine, Path]]):
    compilation_engine, output_path = make_compilation_engine(text)
    compilation_engine.compile_class()
    assert output_path.read_text("utf-8") == expected