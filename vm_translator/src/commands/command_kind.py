from __future__ import annotations
from typing import Any, ClassVar
class VmCmd:
    vm_op2cmd: ClassVar[dict[str, type["VmCmd"]]] = {}
    vm_op: ClassVar[str]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        op = getattr(cls, "vm_op")
        if op:
            if op in VmCmd.vm_op2cmd:
                raise ValueError(f"duplicated ops: {op}")
            VmCmd.vm_op2cmd[op] = cls
        print(op)
    
    def asm_lines(self, label_id: str, file_name: str)-> str:
        raise NotImplementedError