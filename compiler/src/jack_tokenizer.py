from pathlib import Path
from enum import Enum, auto

from protocols import Compiler

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

class JackTokenizer():
    def __init__(self, input_path: Path, compile_engine: Compiler) -> None:
        self.input_path = input_path
        self.piled_jack = Path.read_text(input_path, "utf-8").splitlines()
        self.now_instruction = None
        self.now_token = ""
        self.now_token_type: TOKEN_TYPE | None = None
        self.now_token_keyword = None

    def has_more_token(self) -> bool:
        if len(self.piled_jack) == 0:
            return False
        return True
    
    def tokey_type(self) -> TOKEN_TYPE:
        if not self.now_token_type:
            raise ValueError("now token type is not set")
        return self.now_token_type
    
    def keyword(self) -> KEYWORD:
        if not self.now_token_keyword:
            raise ValueError("now token keyword is not set")
        return self.now_token_keyword
    
    def symbol(self) -> str:
        if self.now_token_type == TOKEN_TYPE.SYMBOL:
            return self.now_token
        else:
            raise ValueError(f"token type should be symbol, but got {self.now_token_type}")

    def identifier(self) -> str:
        if self.now_token_type == TOKEN_TYPE.IDENTIFIER:
            return self.now_token
        else:
            raise ValueError(f"token type should be Identifier, but got {self.now_token_type}")
        
    def intval(self) -> int:
        if self.now_token_type == TOKEN_TYPE.INT_CONST:
            try:
                return int(self.now_token)
            except (ValueError, TypeError):
                raise ValueError((f"token should be able to be integer, but got {self.now_token}"))
        else:
            raise ValueError(f"token type should be INT_CONST, but got {self.now_token_type}")
    
    def string_val(self) -> str:
        if self.now_token_type == TOKEN_TYPE.STRING_CONST:
            return self.now_token
        else:
            raise ValueError(f"token type should be STRING_CONST, but got {self.now_token_type}")