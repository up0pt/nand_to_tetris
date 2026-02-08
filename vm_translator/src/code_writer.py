from pathlib import Path

from commands.arithmetic_command_type import ArithmeticCommands
from commands.memory_access_command_type import Push, Pop
from commands.program_flow_command_type import Label, Goto, If
from commands.function_call_command_type import Function, Call, Return
from commands.command_kind import CommandKind

class CodeWriter:
    def __init__(self, path: Path) -> None:
        self.path = Path

    def set_file_name(self, filename: str) -> None:
        """
        用途がまだわからない．
        
        :param self: 説明
        :param filename: 説明
        :type filename: str
        """
        self.file_name = filename

    def write_arithmetic(self, command: ArithmeticCommands) -> None:
        

    def write_push_pop(self, command: PushOrPop, segment: Segment, index: int) -> None:
        if command not in [VMCommandKind.C_PUSH, VMCommandKind.C_POP]:
            raise ValueError(
                f"command must be either C_PUSH or C_POP, though it was {command}"
            )
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError
