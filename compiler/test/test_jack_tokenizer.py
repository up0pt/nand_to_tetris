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
        ("return 123", (0, 5)),
        ("   \n   {02}  ", (7, 7)),
        ("   \n \n kx_1_2z  ", (7, 13)),
        ("0\n 11", (0, 0)),
        ('      xyz123kk', (6, 13)),
        ("\n  while", (3, 7)),
    ],
)
def test_advance_skip_whitespace(make_tokenizer: Callable[[str], JackTokenizer], text: str, expected: tuple[int, int]):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.now_idx() == expected

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("return(123)", (0, 5)),
        ("   \n   {02}  ", (7, 7)),
        ("   \n \n kx;_1_2z  ", (7, 8)),
    ],
)
def test_advance_skip_whitespace_with_symbol(make_tokenizer: Callable[[str], JackTokenizer], text: str, expected: tuple[int, int]):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.now_idx() == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("return 123", "keyword"),
        ("   \n   {02}  ", "symbol"),
        ("   \n \n kx_1_2z  ", "identifier"),
        ("0\n 11", "int_const"),
        ('   "xyz123kk"', "string_const")
    ],
)
def test_token_type(make_tokenizer: Callable[[str], JackTokenizer], text: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.token_type().value == expected

@pytest.mark.parametrize(
    ("text", "token",  "expected"),
    [
        ("do 1\n    while True", "keyword", "do"),
    ]
)
def test_keyword_methods(make_tokenizer: Callable[[str], JackTokenizer], text: str, token: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.token_type().value == token
    assert jack_tokenizer.keyword() == expected


@pytest.mark.parametrize(
    ("text", "token",  "expected"),
    [
        (" \n   {a1_k}", "symbol", "{"),
    ]
)
def test_symbol_methods(make_tokenizer: Callable[[str], JackTokenizer], text: str, token: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.token_type().value == token
    assert jack_tokenizer.symbol() == expected

@pytest.mark.parametrize(
    ("text", "token",  "expected"),
    [
        (" \n\n _aW2u4()", "identifier", "_aW2u4"),
    ]
)
def test_identifier_methods(make_tokenizer: Callable[[str], JackTokenizer], text: str, token: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.token_type().value == token
    assert jack_tokenizer.identifier() == expected

@pytest.mark.parametrize(
    ("text", "token",  "expected"),
    [
        (" \n\n 3220 _aW2u4()", "int_const", "3220"),
    ]
)
def test_int_const_methods(make_tokenizer: Callable[[str], JackTokenizer], text: str, token: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.token_type().value == token
    assert jack_tokenizer.intval() == expected

@pytest.mark.parametrize(
    ("text", "token",  "expected"),
    [
        (' \n\n "Test_2329()*^&%@!"3220 _aW2u4() "None"', "string_const", '"Test_2329()*^&%@!"'),
    ]
)
def test_string_const_methods(make_tokenizer: Callable[[str], JackTokenizer], text: str, token: str, expected: str):
    jack_tokenizer = make_tokenizer(text)
    jack_tokenizer.advance()
    assert jack_tokenizer.token_type().value == token
    assert jack_tokenizer.string_val() == expected

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (
            ' \n\n "Test_2329()*^&%@!"3220 \n  _aW2u4({return}) "None"', 
            [
                ['"Test_2329()*^&%@!"', "string_const"],
                ["3220", "int_const"],
                ["_aW2u4", "identifier"],
                ["(", "symbol"],
                ["{", "symbol"],
                ["return", "keyword"],
                ["}", "symbol"],
                [")", "symbol"],
                ['"None"', "string_const"],
            ]
        ),
    ]
)
def test_tokenize_long_input_withot_comments(make_tokenizer: Callable[[str], JackTokenizer], text: str, expected: list[list[str]]):
    jack_tokenizer = make_tokenizer(text)
    idx = 0
    while jack_tokenizer.has_more_token():
        jack_tokenizer.advance()
        print(jack_tokenizer.token)
        assert jack_tokenizer.token_type() == expected[idx][1]
        assert jack_tokenizer.token == expected[idx][0]
        idx += 1