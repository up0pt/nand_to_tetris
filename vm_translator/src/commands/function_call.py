from dataclasses import dataclass,field
from typing import ClassVar
from command_kind import VmCmd

NUM_STORED_FUNCTION_STATE: int = 5 # RET, LCL, ARG, THIS, THAT


@dataclass(frozen=True)
class Function(VmCmd):
    vm_op: ClassVar[str] = "function"
    func_name: str
    raw_local_val_num: str

    local_val_num: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "local_val_num", int(self.raw_local_val_num))
    
    def asm_lines(self, label_id: str, file_name: str) -> str:
        return f"""
({file_name}.{self.func_name})
"""+"""
@SP
A=M
M=0
@SP
M=M+1
"""*self.local_val_num



@dataclass(frozen=True)
class Call(VmCmd):
    vm_op: ClassVar[str] = "call"
    func_name: str
    raw_args_num: str

    args_num: int

    def __post_init__(self):
        object.__setattr__(self, "args_num", int(self.raw_args_num))

    def asm_lines(self, label_id: str, file_name: str) -> str:
        ret_label_name = f"{file_name}.{self.func_name}.{label_id}.RET"
        return f"""
// [call {self.func_name} {self.args_num}] push return-address
@{ret_label_name}
D=A
@SP
A=M
M=D
@SP
M=M+1
//[call {self.func_name} {self.args_num}] push LCL, push ARG, push THIS, push THAT
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

//[call {self.func_name} {self.args_num}] set ARG and LCL
@SP
D=M
@LCL
M=D
@{self.args_num + NUM_STORED_FUNCTION_STATE}
D=D-A
@ARG
M=D
@{file_name}.{self.func_name}
0;JMP
({ret_label_name})
"""

@dataclass(frozen=True)
class Return(VmCmd):
    vm_op: ClassVar[str] = "return"
