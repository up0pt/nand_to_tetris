from dataclasses import dataclass
from command_kind import VmCmd

@dataclass(frozen=True)
class Add(VmCmd):
    vm_op: str = "add"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
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
    vm_op: str = "sub"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
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
    vm_op: str = "neg"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
        return """
        @SP
        A=M-1
        M=!M
        M=M+1
        """
    
@dataclass(frozen=True)
class Eq:
    vm_op: str = "eq"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
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
    vm_op: str = "gt"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
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
    vm_op: str = "lt"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
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
    vm_op: str = "and"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
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
    vm_op: str = "or"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
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
    vm_op: str = "not"
    vm_args: list[str] = []
    def asm_lines(self, label_id: str):
        return """
        @SP
        A=M-1
        M=!M
        """