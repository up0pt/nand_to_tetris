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

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("return 123", 0),
        ("   \n   {02}  ", 7),
        ("   \n \n kx_1_2z  ", 7),
        ("0\n 11", 0),
        ('      xyz123kk', 6),
        ("\n  while", 3),
    ],
)
def test_advance_skip_whitespace(make_tokenizer: Callable[[str], JackTokenizer], text: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.now_idx() == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("return 123", "KEYWORD"),
        ("   \n   {02}  ", "SYMBOL"),
        ("   \n \n kx_1_2z  ", "IDENTIFIER"),
        ("0\n 11", "INT_CONST"),
        ('   xyz123kk', "STRING_CONST")
    ],
)
def test_token_type(text: str, expected: str):
    return None