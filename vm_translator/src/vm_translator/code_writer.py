from pathlib import Path
from typing import Literal

from vm_translator.vm_command_type import VMCommandKind
from vm_translator.segment import Segment

type PushOrPop = Literal[VMCommandKind.C_PUSH, VMCommandKind.C_POP]


class CodeWriter:
    def __init__(self, path: Path) -> None:
        self.path = Path

    def set_file_name(self, filename: str) -> None:
        pass

    def write_arithmetic(self, command: str) -> None:
        pass

    def write_push_pop(self, command: PushOrPop, segment: Segment, index: int) -> None:
        if command not in [VMCommandKind.C_PUSH, VMCommandKind.C_POP]:
            raise ValueError(
                f"command must be either C_PUSH or C_POP, though it was {command}"
            )
        pass

    def close(self) -> None:
        pass
