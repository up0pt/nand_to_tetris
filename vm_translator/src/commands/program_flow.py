from dataclasses import dataclass


@dataclass(frozen=True)
class Label:
    symbol: str
    op_str: str = "label"


@dataclass(frozen=True)
class Goto:
    symbol: str
    op_str: str = "goto"


@dataclass(frozen=True)
class If:
    symbol: str
    op_str: str = "if-goto"
