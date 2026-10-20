import pytest
from pathlib import Path

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("return 123", ""),
        ("", 0),
        ("", 32767),
    ],
)
def test_jack_tokenizer_init(tmp_path: Path, text: str, expected: str):
    input_path = tmp_path / "Main.jack"
    input_path.write_text(
        text,
        encoding="utf-8",
    )

    raise NotImplementedError()