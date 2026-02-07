from typing import Union

from commands.arithmetic_command_type import ArithmeticCommands
from commands.memory_access_command_type import Push, Pop
from commands.program_flow_command_type import Label, Goto, If
from commands.function_call_command_type import Function, Call, Return

CommandKind = Union[
    ArithmeticCommands, Push, Pop, Label, Goto, If, Function, Call, Return
]