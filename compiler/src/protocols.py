from typing import Protocol
from pathlib import Path

class Compiler(Protocol):
    def __init__(self, output_path: Path)-> None:
        ...

    def compile_class(self) -> None:
        ...