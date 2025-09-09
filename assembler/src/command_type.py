from typing import Final, Literal

A_COMMAND: Final = "A_COMMAND"
C_COMMAND: Final = "C_COMMAND"
L_COMMAND: Final = "L_COMMAND"

type CommandKind = Literal["A_COMMAND", "C_COMMAND", "L_COMMAND"]
