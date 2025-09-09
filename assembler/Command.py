from typing import TypedDict, Literal, Union
from Binary import Bit, Bit3, Bit7

class A_COMMAND(TypedDict):
    kind: Literal["A_COMMAND"]
    addr: tuple[
        Bit, Bit, Bit, Bit, Bit,
        Bit, Bit, Bit, Bit, Bit,
        Bit, Bit, Bit, Bit, Bit,
        ] # #Bit = 15

class C_COMMAND(TypedDict):
    kind: Literal["C_COMMAND"]
    dest: Bit3
    comp: Bit7
    jump: Bit3

class L_COMMAND(TypedDict):
    kind: Literal["L_COMMAND"]


COMMAND = Union[A_COMMAND, C_COMMAND, L_COMMAND]