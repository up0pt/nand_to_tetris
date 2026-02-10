from dataclasses import dataclass
from command_kind import VmCmd


@dataclass(frozen=True)
class Function(VmCmd):
    vm_args: tuple[str, int]
    vm_op: str = "function"


@dataclass(frozen=True)
class Call(VmCmd):
    vm_args: tuple[str, int]
    vm_op: str = "call"


@dataclass(frozen=True)
class Return(VmCmd):
    vm_args: None = None
    vm_op: str = "return"
