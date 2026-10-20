from pathlib import Path
from enum import Enum, auto

class TOKEN_TYPE(Enum):
    KEYWORD = auto()
    SYMBOL = auto()
    IDENTIFIER = auto()
    INT_CONST = auto()
    STRING_CONST = auto()

class KEYWORD(Enum):
    CLASS = auto()
    METHOD = auto()
    FUNCTION = auto()
    CONSTRUCTOR = auto()
    INT = auto()
    BOOLEAN = auto()
    CHAR = auto()
    VOID = auto()
    VAR = auto()
    STATIC = auto()
    FIELD = auto()
    LET = auto()
    DO = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    RETURN = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    THIS = auto()

class SYMBOL(Enum):
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACKET = "["
    RIGHT_BRACKET = "]"
    DOT = "."
    COMMA = ","
    SEMICOLON = ";"
    PLUS = "+"
    MINUS = "-"
    ASTERISK = "*"
    SLASH = "/"
    AMPERSAND = "&"
    PIPE = "|"
    LESS_THAN = "<"
    GREATER_THAN = ">"
    EQUAL = "="
    TILDE = "~"

SYMBOL_SET = {symbol.value for symbol in SYMBOL}
BLANK_SET = {" ", "\n", "\t"}

class JackTokenizer():
    def __init__(self, input_path: Path) -> None:
        self.input_path = input_path
        self.piled_jack_chars = Path.read_text(input_path, "utf-8")
        self.token_start_idx = 0
        self.token_end_idx = 0

    def _is_start_idx_ltn_len(self) -> bool:
        return self.token_start_idx+1 < len(self.piled_jack_chars)

    def has_more_token(self) -> bool:
        while self._is_start_idx_ltn_len() and self.piled_jack_chars[self.token_start_idx+1] in BLANK_SET:
            self.token_start_idx += 1

        return self._is_start_idx_ltn_len()
        
    def advance(self) -> None:
        raise NotImplementedError()
    
    def token_type(self) -> TOKEN_TYPE:
        raise NotImplementedError()
    
    def keyword(self) -> KEYWORD:
        raise NotImplementedError()
    
    def symbol(self) -> str:
        raise NotImplementedError()

    def identifier(self) -> str:
        raise NotImplementedError()
        
    def intval(self) -> int:
        raise NotImplementedError()
    
    def string_val(self) -> str:
        raise NotImplementedError()