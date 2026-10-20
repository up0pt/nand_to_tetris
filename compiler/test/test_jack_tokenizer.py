import pytest
from pathlib import Path
from collections.abc import Callable
from jack_tokenizer import JackTokenizer

@pytest.fixture
def make_tokenizer(tmp_path: Path) -> Callable[[str], JackTokenizer]:
    def make(input_text: str) -> JackTokenizer:
        input_path = tmp_path / "Main.jack"
        input_path.write_text(
            input_text,
            encoding="utf-8"
        )
        return JackTokenizer(input_path)

    return make

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("return 123", True),
        ("0\n 11", True),
        ("   \n     ", False),
    ],
)
def test_has_more_token(make_tokenizer: Callable[[str], JackTokenizer], text: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    assert jack_tokenizer.has_more_token() == expected