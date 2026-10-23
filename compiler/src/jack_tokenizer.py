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

    @classmethod
    def is_keyword(cls, text: str) -> bool:
        return text in {keyword.value for keyword in Keyword}

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

    @classmethod
    def is_symbol(cls, text: str) -> bool:
        return text in {symbol.value for symbol in Symbol}

class Identifier(str):
    def __new__(cls, text: str) -> "Identifier":
        if not Identifier.is_identifier(text):
            raise ValueError(f"Invalid identifier: {text!r}")
        return super().__new__(cls, text)
    
    @classmethod
    def is_identifier(cls, text: str) -> bool:
        return re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", text) is not None

class IntConst(str):
    def __new__(cls, text: str) -> "IntConst":
        if not IntConst.is_int_const(text):
            raise ValueError(f"Invalid identifier: {text!r}")
        return super().__new__(cls, text)

    @classmethod
    def is_int_const(cls, text: str) -> bool:
        return re.fullmatch(r"[0-9]+", text) is not None and 0 <= int(text) <= 32767 # Don't use r"\d+". In python, \d matches full-width charactors, too.

class StringConst(str):
    def __new__(cls, text: str) -> "StringConst":
        if not StringConst.is_string_const(text):
            raise ValueError(f"Invalid StringConst: {text!r}")

        return super().__new__(cls, text)
    
    @classmethod
    def is_string_const(cls, token: str) -> bool:
        return token.isascii() and re.fullmatch(r'"[^"\r\n]*"', token) is not None

BLANK_SET = {" ", "\n", "\t"}

class JackTokenizer():
    def __init__(self, input_path: Path) -> None:
        self.input_path = input_path
        self.piled_jack_chars = Path.read_text(input_path, "utf-8")
        self._token_start_idx = 0
        self._token_end_idx = -1
        self.token = None

    def _is_idx_ltn_len(self, idx: int) -> bool:
        return idx < len(self.piled_jack_chars)

    def _skip_whitespace_and_comments(self, start_idx: int) -> int:
        while self._is_idx_ltn_len(start_idx) and self.piled_jack_chars[start_idx] in BLANK_SET:
            start_idx += 1

        return start_idx

    def _skip_before_whitespace_or_comments(self, end_idx: int) -> int:
        start_with = self.piled_jack_chars[end_idx]
        if Symbol.is_symbol(start_with):
            return end_idx
        
        while self._is_idx_ltn_len(end_idx+1) and self.piled_jack_chars[end_idx+1] not in BLANK_SET:
            if start_with != '"' and Symbol.is_symbol(self.piled_jack_chars[end_idx+1]):
                return end_idx
            
            if start_with == '"' and self.piled_jack_chars[end_idx+1] == '"':
                return end_idx + 1
            
            end_idx += 1
        
        return end_idx

    def now_idx(self) -> tuple[int,int]:
        return (self._token_start_idx, self._token_end_idx)

    def has_more_token(self) -> bool:
        start_idx = self._skip_whitespace_and_comments(self._token_end_idx+1)
        return self._is_idx_ltn_len(start_idx)
        
    def advance(self) -> None:
        if self.has_more_token():
            self._token_start_idx = self._skip_whitespace_and_comments(self._token_end_idx+1)
            self._token_end_idx = self._skip_before_whitespace_or_comments(self._token_start_idx)
    
    def token_type(self) -> TokenType:
        token_text = self.piled_jack_chars[self._token_start_idx : self._token_end_idx+1]
        self._set_token(token_text)

        if Keyword.is_keyword(self._get_token()):
            return TokenType.KEYWORD
        elif Symbol.is_symbol(self._get_token()):
            return TokenType.SYMBOL
        elif Identifier.is_identifier(self._get_token()):
            return TokenType.IDENTIFIER
        elif IntConst.is_int_const(self._get_token()):
            return TokenType.INT_CONST
        elif StringConst.is_string_const(self._get_token()):
            return TokenType.STRING_CONST
        else:
            raise NotImplementedError(f"{self._get_token()} is not recognized as Token")

    def _get_token(self) -> str:
        token = self.token
        if token is None:
            raise RuntimeError(
                "No current token. Call advance() successfully first."
            )
        return token

    def _set_token(self, token: str) -> None:
        self.token = token
    
    def keyword(self) -> Keyword:
        return Keyword(self._get_token())
    
    def symbol(self) -> Symbol:
        return Symbol(self._get_token())

    def identifier(self) -> Identifier:
        return Identifier(self._get_token())
        
    def intval(self) -> IntConst:
        return IntConst(self._get_token())
    
    def string_val(self) -> StringConst:
        return StringConst(self._get_token())