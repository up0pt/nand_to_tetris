from typing import Protocol
from pathlib import Path

class Compiler(Protocol):
    def __init__(self, input_path: Path)-> None:
        ...

    def compileClass(self) -> None:
        ...
    
    def compileVarDec(self) -> None:
        ...
    
    def compileSubroutine(self) -> None:
        ...