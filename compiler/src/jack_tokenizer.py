from pathlib import Path

class JackTokenizer():
    def __init__(self, input_path: Path) -> None:
        self.input_path = input_path
        self.piled_jack = Path.read_text(input_path, "utf-8").splitlines()
        self.now_instruction = None

    def has_more_token(self) -> bool:
        if len(self.piled_jack) == 0:
            return False
        raise NotImplementedError