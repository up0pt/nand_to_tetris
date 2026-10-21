from pathlib import Path
from enum import Enum, auto, StrEnum
import re

class TOKEN_TYPE(StrEnum):
    KEYWORD = auto()
    SYMBOL = auto()
    IDENTIFIER = auto()
    INT_CONST = auto()
    STRING_CONST = auto()

class KEYWORD(StrEnum):
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
KEYWORD_SET = {keyword.value for keyword in KEYWORD}
BLANK_SET = {" ", "\n", "\t"}

class JackTokenizer():
    def __init__(self, input_path: Path) -> None:
        self.input_path = input_path
        self.piled_jack_chars = Path.read_text(input_path, "utf-8")
        self._token_start_idx = 0
        self._token_end_idx = 0

    def _is_idx_ltn_len(self, idx: int) -> bool:
        return idx < len(self.piled_jack_chars)

    def _skip_whitespace_and_comments(self, start_idx: int) -> int:
        while self._is_idx_ltn_len(start_idx) and self.piled_jack_chars[start_idx] in BLANK_SET:
            start_idx += 1

        return start_idx

    def _skip_before_whitespace_or_comments(self, end_idx: int) -> int:
        if self.piled_jack_chars[end_idx] in SYMBOL_SET:
            return end_idx
        
        while self._is_idx_ltn_len(end_idx+1) and self.piled_jack_chars[end_idx+1] not in BLANK_SET:
            if self.piled_jack_chars[end_idx+1] in SYMBOL_SET:
                return end_idx
            end_idx += 1
        
        return end_idx

    def now_idx(self) -> tuple[int,int]:
        return (self._token_start_idx, self._token_end_idx)

    def has_more_token(self) -> bool:
        start_idx = self._skip_whitespace_and_comments(self._token_start_idx)
        return self._is_idx_ltn_len(start_idx)
        
    def advance(self) -> None:
        if self.has_more_token():
            self._token_start_idx = self._skip_whitespace_and_comments(self._token_start_idx)
            self._token_end_idx = self._skip_before_whitespace_or_comments(self._token_start_idx)
    
    def token_type(self) -> TOKEN_TYPE:
        token = self.piled_jack_chars[self._token_start_idx : self._token_end_idx+1]

        match token:
            case _ if token in SYMBOL_SET:
                return TOKEN_TYPE.SYMBOL
            case _ if token in KEYWORD_SET:
                return TOKEN_TYPE.KEYWORD
            case _ if re.match(r"\d+", token):
                return TOKEN_TYPE.INT_CONST
            case _ :
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