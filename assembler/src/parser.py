from pathlib import Path
import re

from command_type import A_COMMAND, C_COMMAND, L_COMMAND, CommandKind

COMMENT_SEP = "//"

class Parser():
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        self.dirty_commands: list[str] = self.path.read_text().split('\n')

    def hasMoreCommands(self) -> bool:
        return bool(len(self.dirty_commands))
    
    def advance(self) -> None:
        self.dirty_commands.pop(0) # raise IndexError if self.dirty_commands is empty.
    
    def get_latest_clean_command(self) -> str:
        command = self.dirty_commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        return clean_command
    
    def commandType(self) -> CommandKind | None:
        clean_command = self.get_latest_clean_command()
        if clean_command == "":
            return None
        match clean_command[0]:
            case "@":
                return A_COMMAND
            case "(":
                return L_COMMAND
            case _:
                return C_COMMAND
    
    def symbol(self) -> str:
        clean_command = self.get_latest_clean_command()
        match clean_command[0]:
            case "@":
                return clean_command[1:]
            case "(":
                return clean_command[1:-1]
            case _:
                raise NotImplementedError()
    
    def dest(self) -> str:
        clean_command = self.get_latest_clean_command()
        if "=" in clean_command:
            return clean_command.split("=", 1)[0]
        elif ";" in clean_command:
            return "null"
        else:
            raise ValueError()
    
    def comp(self) -> str:
        clean_command = self.get_latest_clean_command()
        if "=" in clean_command:
            return clean_command.split("=", 1)[1]
        elif ";" in clean_command:
            if clean_command.split(";", 1)[0] == "D":
                return "D"
            elif clean_command.split(";", 1)[0] == "0":
                return "0"
            else:
                raise ValueError("The computation before jump instruction must be either D or 0.")
        else:
            raise ValueError("The computation command must have = or ; expression.")

    
    def jump(self) -> str:
        command =  self.dirty_commands[0]
        clean_command = re.sub(r"\s+", "", command.split(COMMENT_SEP, 1)[0])
        splits = clean_command.split(";", 1)
        if len(splits) == 2:
            return splits[1]
        else:
            return "null"
        
if __name__ == "__main__":
    p = Path('/Users/masaki/Develop/learn/nand_to_tetris/assembler/test/inputs/plain_1.txt')
    parser = Parser(p)