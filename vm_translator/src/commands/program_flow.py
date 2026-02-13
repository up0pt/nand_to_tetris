from dataclasses import dataclass
import re
from typing import ClassVar

from command_kind import VmCmd

@dataclass(frozen=True)
class Label(VmCmd):
    vm_op: ClassVar[str] = "label"
    label_name: str

    def asm_lines(self, label_id: str, file_name: str):
        if re.fullmatch(r"^(?!\d)[a-zA-Z0-9_.:]+", self.label_name):
            return f"""
({file_name}.{self.label_name})
            """
        else:
            raise ValueError("Label name should not start with digit and as a whole, it should use only digit, alphabet (Capitalized or lower), or symbols (_.:)")


@dataclass(frozen=True)
class Goto(VmCmd):
    vm_op: ClassVar[str] = "goto"
    distination: str
    def asm_lines(self, label_id: str, file_name: str) -> str:
        return f"""
@{file_name}.{self.distination}
0;JMP
        """


@dataclass(frozen=True)
class If(VmCmd):
    vm_op: ClassVar[str] = "if-goto"
    distination: str
    def asm_lines(self, label_id: str, file_name: str) -> str:
        return f"""
@SP
AM=M-1
D=M
@{file_name}.{self.distination}
D;JMP
"""