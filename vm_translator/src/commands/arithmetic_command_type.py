from enum import Enum, auto
from typing import cast

class ArithmeticCommands(Enum):
    def _generate_next_value_(name: str, start, count, last_values) -> str:
        return str.lower(name)
    ADD = auto()
    SUB = auto()
    NEQ = auto()
    EQ = auto()
    GT = auto()
    LT = auto()
    AND = auto()
    OR = auto()
    NOT = auto()

ARITH_VALUES: set[str] = {cast(str, e.value) for e in ArithmeticCommands}