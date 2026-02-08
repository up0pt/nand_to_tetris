from typing import Protocol

class Command(Protocol):
    vm_ops: str
    vm_ops_split: list[str | int]
    def asm_lines(self)-> str:
        """
        asm_lines の Docstring
        
        :param self:
        :return: vm command に対応する asm の command lines
        :rtype: str
        """
        ...