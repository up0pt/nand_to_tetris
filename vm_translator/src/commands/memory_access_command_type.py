from dataclasses import dataclass
from enum import Enum, auto, unique


@unique
class Segment(Enum):
    def _generate_next_value_(name: str, *_):
        return str.lower(name)

    ARGUMENT = auto()
    LOCAL = auto()
    STATICC = auto()
    CONSTANT = auto()
    THIS = auto()
    THAT = auto()
    POINTER = auto()
    TMEP = auto()


@dataclass(frozen=True)
class Push:
    seg: Segment
    index: int
    op_str: str = "push"


@dataclass(frozen=True)
class Pop:
    seg: Segment
    index: int
    op_str: str = "pop"
