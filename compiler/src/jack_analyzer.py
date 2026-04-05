from pathlib import Path

class JackAnalyzer():
    def __init__(self, inputs: Path) -> None:
        raise NotImplementedError

    def parse(self) -> None:
        raise NotImplementedError
    

if __name__ == "__main__":
    input_path = None
    jackanalyzer = JackAnalyzer(input_path)