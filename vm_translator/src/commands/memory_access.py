from dataclasses import dataclass, field, InitVar
from enum import Enum, auto, unique
from typing import ClassVar
from .command_kind import VmCmd
from .predefined_symbols import (generic_Register1, generic_Register2, generic_Register3)


@unique
class Segment(Enum):
    def _generate_next_value_(name: str, *_):
        return str.lower(name)

    ARGUMENT = auto()
    LOCAL = auto()
    STATIC = auto()
    CONSTANT = auto()
    THIS = auto()
    THAT = auto()
    POINTER = auto()
    TEMP = auto()


@dataclass(frozen=True)
class Push(VmCmd):
    vm_op: ClassVar[str] = "push"
    raw_segment: str
    raw_index: str

    segment: Segment = field(init=False)
    index: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "segment", Segment(self.raw_segment))
        object.__setattr__(self, "index", int(self.raw_index))

    def asm_lines(self, label_id: str, file_name: str) -> str:
        match self.segment:
            case Segment.ARGUMENT:
                return f"""
@ARG
D=M
@{self.index}
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                """
            case Segment.LOCAL:
                return f"""
@LCL
D=M
@{self.index}
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                """
            case Segment.STATIC:
                return f"""
@{file_name}.{self.index}
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                """
            case Segment.CONSTANT:
                return f"""
@{self.index}
D=A
@SP
A=M
M=D
@SP
M=M+1
D=0
                """
            case Segment.THIS:
                return f"""
@THIS
D=M
@{self.index}
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                """
            case Segment.THAT:
                return f"""
@THAT
D=M
@{self.index}
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                """
            case Segment.POINTER:
                if self.index in [0, 1]:
                    return f"""
@{3 + self.index}
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                    """
                else:
                    raise ValueError(f"push pointer x: x should be 0(THIS) or 1(THAT), but given {self.index}")
            case Segment.TEMP:
                return f"""
@5
D=A
@{self.index}
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
D=0
                """ 
            case _:
                raise ValueError



@dataclass(frozen=True)
class Pop(VmCmd):
    vm_op: ClassVar[str] = "pop"
    raw_segment: str
    raw_index: str

    segment: Segment = field(init=False)
    index: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "segment", Segment(self.raw_segment))
        object.__setattr__(self, "index", int(self.raw_index))

    def asm_lines(self, label_id: str, file_name: str) -> str:
        match self.segment:
            case Segment.ARGUMENT:
                return f"""
@SP
AM=M-1
D=M
M=0
@{generic_Register1}
M=D
@ARG
D=M
@{self.index}
D=D+A
@{generic_Register2}
M=D
@{generic_Register1}
D=M
@{generic_Register2}
A=M
M=D
                """
            case Segment.LOCAL:
                return f"""
@SP
AM=M-1
D=M
M=0
@{generic_Register1}
M=D
@LCL
D=M
@{self.index}
D=D+A
@{generic_Register2}
M=D
@{generic_Register1}
D=M
@{generic_Register2}
A=M
M=D
                """
            case Segment.STATIC:
                return f"""
@SP
AM=M-1
D=M
M=0
@{file_name}.{self.index}
M=D
                """
            case Segment.CONSTANT:
                raise NotImplementedError
            case Segment.THIS:
                return f"""
@SP
AM=M-1
D=M
M=0
@{generic_Register1}
M=D
@THIS
D=M
@{self.index}
D=D+A
@{generic_Register2}
M=D
@{generic_Register1}
D=M
@{generic_Register2}
A=M
M=D
                """
            case Segment.THAT:
                return f"""
@SP
AM=M-1
D=M
M=0
@{generic_Register1}
M=D
@THAT
D=M
@{self.index}
D=D+A
@{generic_Register2}
M=D
@{generic_Register1}
D=M
@{generic_Register2}
A=M
M=D
                """
            case Segment.POINTER:
                if self.index in [0,1]:
                    return f"""
@SP
AM=M-1
D=M
M=0
@{3+self.index}
M=D
                    """
                else:
                    raise ValueError(f"pop pointer x: x should be 0(THIS) or 1(THAT), but given {self.index}")
            case Segment.TEMP:
                if self.index in [x for x in range(8)]:
                    return f"""
@SP
AM=M-1
D=M
M=0
@{5+self.index}
M=D
                    """
                else:
                    raise ValueError(f"pop temp x: x should be 0..7, but given {self.index}")
            case _:
                raise NotImplementedError