from dataclasses import dataclass

@dataclass(frozen=True)
class Function:
    func_name: str
    n_locals: int
    op_str: str =  "function"

@dataclass(frozen=True)
class Call:
    func_name: str
    n_args: int
    op_str: str = "call"

@dataclass(frozen=True)
class Return:
    op_str: str = "return"