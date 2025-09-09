from pathlib import Path
from typing import Final, Literal
import re

A_COMMAND: Final = "A_COMMAND"
C_COMMAND: Final = "C_COMMAND"
L_COMMAND: Final = "L_COMMAND"

type CommandKind = Literal["A_COMMAND", "C_COMMAND", "L_COMMAND"]
COMMENT_SEP = "//"

class Parser():
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        # str_pathのPathインスタンス化、エラーハンドリングはmainに押し付ける
        self.commands: list[str] = self.path.read_text().split('\n')

    def hasMoreCommands(self) -> bool:
        return bool(len(self.commands))
    
    def advance(self) -> None:
        self.commands.pop(0) # raise IndexError if self.commands is empty.
    
    def commandType(self) -> CommandKind | None:
        command = self.commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        if clean_command == "":
            return None
        match clean_command[0]:
            case "@":
                return A_COMMAND
            case "(":
                return L_COMMAND
            case _:
                return C_COMMAND
            
    def get_latest_clean_command(self) -> str:
        command = self.commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        return clean_command
    
    def symbol(self) -> str:
        command = self.commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        match clean_command[0]:
            case "@":
                return clean_command[1:]
            case "(":
                return clean_command[1:-1]
            case _:
                raise NotImplementedError()
    
    def dest(self) -> str:
        command =  self.commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        if "=" in clean_command:
            return clean_command.split("=", 1)[0]
        elif ";" in clean_command:
            return "null"
        else:
            raise ValueError()
    
    def comp(self) -> str:
        command =  self.commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        if "=" in clean_command:
            return clean_command.split("=", 1)[1]
        elif ";" in clean_command:
            if clean_command.split(";", 1)[0] == "D":
                return "D"
            if clean_command.split(";", 1)[0] == "0":
                return "0"
        else:
            raise ValueError()

    
    def jump(self) -> str:
        command =  self.commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        splits = clean_command.split(";", 1)
        if len(splits) == 2:
            return splits[1]
        elif len(splits) == 1:
            return "null"
        else:
            raise ValueError()
    
if __name__ == "__main__":
    p = Path('/Users/masaki/Develop/learn/nand_to_tetris/assembler/test/inputs/plain_1.txt')
    parser = Parser(p)