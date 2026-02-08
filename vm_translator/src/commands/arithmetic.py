from dataclasses import dataclass
from typing import ClassVar
from command_kind import VmCmd

@dataclass(frozen=True)
class Add(VmCmd):
    vm_op: ClassVar[str] = "add"
    def asm_lines(self, label_id: str, *_):
        return """
        @SP
        AM=M-1
        D=M
        M=0
        @SP
        AM=M-1
        M=D+M
        D=0
        """

@dataclass(frozen=True)
class Sub:
    vm_op: ClassVar[str] = "sub"
    def asm_lines(self, label_id: str, *_):
        return """
        @SP
        AM=M-1
        D=M
        M=0
        @SP
        AM=M-1
        M=M-D
        D=0
        """
    
@dataclass(frozen=True)
class Neg:
    vm_op: ClassVar[str] = "neg"
    def asm_lines(self, label_id: str, *_):
        return """
        @SP
        A=M-1
        M=!M
        M=M+1
        """
    
@dataclass(frozen=True)
class Eq:
    vm_op: ClassVar[str] = "eq"
    def asm_lines(self, label_id: str, *_):
        return f"""
        @SP
        AM=M-1
        D=M
        M=0
        A=A-1
        D=D-M
        M=0
        @END_{label_id}
        D;JNE
        @SP
        A=M-1
        M=-1
        (END_{label_id})
        D=0
        """

@dataclass(frozen=True)
class Gt:
    vm_op: ClassVar[str] = "gt"
    def asm_lines(self, label_id: str, *_):
        return f"""
        @SP
        AM=M-1
        D=M
        M=0
        A=A-1
        D=D-M
        M=-1
        @END_{label_id}
        D;JLT
        @SP
        A=M-1
        M=0
        (END_{label_id})
        D=0
        """

@dataclass(frozen=True)
class Lt:
    vm_op: ClassVar[str] = "lt"
    def asm_lines(self, label_id: str, *_):
        return f"""
        @SP
        AM=M-1
        D=M
        M=0
        A=A-1
        D=D-M
        M=-1
        @END_{label_id}
        D;JGT
        @SP
        A=M-1
        M=0
        (END_{label_id})
        D=0
        """
    
@dataclass(frozen=True)
class And:
    vm_op: ClassVar[str] = "and"
    def asm_lines(self, label_id: str, *_):
        return """
        @SP
        AM=M-1
        D=M
        M=0
        A=A-1
        M=D&M
        D=0
        """
    
@dataclass(frozen=True)
class Or:
    vm_op: ClassVar[str] = "or"
    def asm_lines(self, label_id: str, *_):
        return """
        @SP
        AM=M-1
        D=M
        M=0
        A=A-1
        M=D|M
        D=0
        """

@dataclass(frozen=True)
class Not:
    vm_op: ClassVar[str] = "not"
    def asm_lines(self, label_id: str, *_):
        return """
        @SP
        A=M-1
        M=!M
        """