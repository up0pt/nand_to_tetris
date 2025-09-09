from typing import Literal, TypeAlias, Any

bit1: TypeAlias = Literal[0, 1]


class Bit:
    def __init__(self, content: tuple[bit1]) -> None:
        self.content = content

    def __str__(self) -> str:
        return "".join(map(str, self.content))

    def __radd__(self, other: Any):
        if isinstance(other, str):
            return other + str(self)
        return NotImplemented

    def __add__(self, other: Any):
        if isinstance(other, str):
            return str(self) + other
        return NotImplemented


class Bit3(Bit):
    def __init__(self, content: tuple[bit1, bit1, bit1]) -> None:
        self.content = content


class Bit7(Bit):
    def __init__(
        self, content: tuple[bit1, bit1, bit1, bit1, bit1, bit1, bit1]
    ) -> None:
        self.content = content
