from pathlib import Path
from enum import auto, StrEnum
import re

class TokenType(StrEnum):
    KEYWORD = auto()
    SYMBOL = auto()
    IDENTIFIER = auto()
    INT_CONST = auto()
    STRING_CONST = auto()

class Keyword(StrEnum):
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

class Symbol(StrEnum):
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

class Identifier(str):
    def __new__(cls, text: str) -> "Identifier":
        if not Identifier.is_identifier(text):
            raise ValueError(f"Invalid identifier: {text!r}")
        return super().__new__(cls, text)
    
    @classmethod
    def is_identifier(cls, text: str) -> bool:
        return re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", text) is not None

SYMBOL_SET = {symbol.value for symbol in Symbol}
KEYWORD_SET = {keyword.value for keyword in Keyword}
BLANK_SET = {" ", "\n", "\t"}

class JackTokenizer():
    def __init__(self, input_path: Path) -> None:
        self.input_path = input_path
        self.piled_jack_chars = Path.read_text(input_path, "utf-8")
        self._token_start_idx = 0
        self._token_end_idx = 0
        self.token = None

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

    def _is_int_const(self, token: str) -> bool:
        return re.fullmatch(r"[0-9]+", token) is not None and 0 <= int(token) <= 32767 # Don't use \d. In python, \d matches full-width charactors, too.

    def _is_string_const(self, token: str) -> bool:
        return token.isascii() and re.fullmatch(r'"[^"\r\n]*"', token) is not None
    
    def token_type(self) -> TokenType:
        self.token = self.piled_jack_chars[self._token_start_idx : self._token_end_idx+1]

        if self.token in KEYWORD_SET:
            return TokenType.KEYWORD
        elif self.token in SYMBOL_SET:
            return TokenType.SYMBOL
        elif Identifier.is_identifier(self.token):
            return TokenType.IDENTIFIER
        elif self._is_int_const(self.token):
            return TokenType.INT_CONST
        elif self._is_string_const(self.token):
            return TokenType.STRING_CONST
        else:
            raise NotImplementedError(f"{self.token} is not recognized as Token")
    
    def keyword(self) -> Keyword | None:
        return Keyword(self.token)
    
    def symbol(self) -> Symbol | None:
        return Symbol(self.token)

    def identifier(self) -> str:
        raise NotImplementedError()
        
    def intval(self) -> int:
        raise NotImplementedError()
    
    def string_val(self) -> str:
        raise NotImplementedError()