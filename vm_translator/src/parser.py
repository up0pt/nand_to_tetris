from pathlib import Path

from commands.command_kind import VmCmd
from commands.arithmetic import (
    Add, Sub, Neg, Eq, Gt, Lt, And, Or, Not
)
from commands.memory_access import Segment, Push, Pop

class Parser:
    def __init__(self, input_path: Path) -> None:
        self.path = input_path
        self.piled_commands: list[str] = self.path.read_text(encoding="utf-8").splitlines()
        self.now_command: VmCmd | None = None

    def has_more_commands(self) -> bool:
        """
        ここでadvanceの終了かどうかを確かめるためにcommandを読む必要がある．

        :param self: 説明
        :return: 説明
        :rtype: bool
        """
        while not Parser._remove_comment_from_line(self.piled_commands[0]):
            self.piled_commands.pop(0)
        return len(self.piled_commands) > 0

    def advance(self) -> None:
        if not self.has_more_commands():
            raise RuntimeError("Parser.advance() called with no remaining commands")
        self.now_command = self._segmentation(self.piled_commands.pop(0))

    def command_type(self) -> VmCmd | None:
        return self.now_command

    @staticmethod
    def _remove_comment_from_line(raw_command_line: str) -> str:
        return raw_command_line.split("//", 1)[0].strip()

    @staticmethod
    def _segmentation(raw_command_line: str) -> VmCmd:
        splited_raw_command_line: list[str] = Parser._remove_comment_from_line(
            raw_command_line
        ).split()

        op, *args = splited_raw_command_line

        if len(splited_raw_command_line) == 0:
            raise ValueError
        else:
            return VmCmd.vm_op2cmd[op](*args)
            
