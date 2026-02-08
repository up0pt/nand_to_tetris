from dataclasses import dataclass, field, InitVar
from enum import Enum, auto, unique
from typing import ClassVar
from command_kind import VmCmd


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
    TMEP = auto()


@dataclass(frozen=True)
class Push(VmCmd):
    vm_op: ClassVar[str] = "push"
    raw_segment: str
    raw_index: str

    segment: Segment = field(init=False)
    index: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "segment", Segment(self.raw_segment))
        object.__setattr__(self, "index", Segment(self.raw_index))

    def asm_lines(self, label_id: str) -> str:
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
                @16
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
                if self.index == 0:
                    return """
                    @THIS
                    D=M
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1
                    D=0
                    """
                elif self.index == 1:
                    return """
                    @THAT
                    D=M
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1
                    D=0
                    """
                else:
                    raise ValueError(f"push pointer x: x is 0(THIS) or 1(THAT): given {self.index}")
            case Segment.TMEP:
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
        object.__setattr__(self, "index", Segment(self.raw_index))

    def asm_lines(self, label_id: str) -> str:
        match self.segment:
            case Segment.ARGUMENT:
                generic_Register1 = 13
                generic_Register2 = 14
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