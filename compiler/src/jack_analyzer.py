import sys
from pathlib import Path

from jack_tokenizer import JackTokenizer
from compilation_engine import CompilationEngine

class JackAnalyzer():
    def __init__(self, input_output_paths: list[tuple[Path, Path]]) -> None:
        self.input_output_paths: list[tuple[Path, Path]] = input_output_paths

    def parse_one_file(self) -> None:
        raise NotImplementedError
    
    def parse_all_files(self) -> None:
        for (input, output) in self.input_output_paths:
            compilation_engine = CompilationEngine(output)
            _jack_tokenizer = JackTokenizer(input, compilation_engine)


def file_searcher(input_path: Path, file_extention_glob: str = "*.jack") -> list[Path]:
    if input_path.is_file():
        if input_path.suffix == ".jack":
            return [input_path]
        raise ValueError(f"Input file {input_path} is not jack file!")

    elif input_path.is_dir():
        return sorted(input_path.glob(file_extention_glob))
    
    else:
        raise FileNotFoundError(f"Input file or folder {input_path} is not found.")
    
def make_blank_tokened_file_objects(source_file: list[Path]) -> list[tuple[Path, Path]]:
    return [(file, file.with_suffix(".xml")) for file in source_file]
    
def main():
    args = sys.argv[1]
    input_path = Path(args)

    input_jack_files = file_searcher(input_path)
    input_output_files = make_blank_tokened_file_objects(input_jack_files)

    _jackanalyzer = JackAnalyzer(input_output_files)
