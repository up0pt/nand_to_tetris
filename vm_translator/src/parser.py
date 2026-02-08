from pathlib import Path
from typing import Union

from commands.arithmetic_command_type import (
    Add, Sub, Neg, Eq, Gt, Lt, And, Or, Not
)
from commands.memory_access_command_type import Segment, Push, Pop
from commands.program_flow_command_type import Label, Goto, If
from commands.function_call_command_type import Function, Call, Return
from commands.command_kind import Command

class Parser:
    def __init__(self, path_str: str) -> None:
        self.path = Path(path_str)
        self.piled_commands: list[str] = self.path.read_text(encoding="utf-8").splitlines()
        self.now_command: Command | None = None

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

    def command_type(self) -> Command | None:
        return self.now_command

    @staticmethod
    def _remove_comment_from_line(raw_command_line: str) -> str:
        return raw_command_line.split("//", 1)[0].strip()

    @staticmethod
    def _segmentation(raw_command_line: str) -> Command:
        splited_raw_command_line: list[str] = Parser._remove_comment_from_line(
            raw_command_line
        ).split()

        match splited_raw_command_line:
            case [arith_op] if arith_op in ARITH_VALUES:
                return 
            case [Push.op_str, seg, index]:
                return Push(seg=Segment(seg), index=int(index))
            case [Pop.op_str, seg, index]:
                return Pop(seg=Segment(seg), index=int(index))
            case [Label.op_str, symbol]:
                return Label(symbol=symbol)
            case [Goto.op_str, symbol]:
                return Goto(symbol=symbol)
            case [If.op_str, symbol]:
                return If(symbol=symbol)
            case [Function.op_str, func_name, n_locals]:
                return Function(func_name=func_name, n_locals=int(n_locals))
            case [Call.op_str, func_name, n_args]:
                return Call(func_name=func_name, n_args=n_args)
            case [Return.op_str]:
                return Return()
            case _:
                raise RuntimeError(
                    f"Detected a command {raw_command_line} which doesn't align VM command rules"
                )
