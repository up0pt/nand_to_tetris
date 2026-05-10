from pathlib import Path

class CompilationEngine():
    def __init__(self, output_path: Path) -> None:
        raise NotImplementedError
    
    def compile_class(self) -> None:
        raise NotImplementedError