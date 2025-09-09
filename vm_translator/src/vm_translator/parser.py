from vm_command_type import VMCommandKind


class Parser:
    def __init__(self) -> None:
        pass

    def has_more_commands(self) -> bool:
        pass

    def advance(self) -> None:
        pass

    def command_type(self) -> VMCommandKind:
        pass

    def arg1(self) -> str:
        pass

    def arg2(self) -> int:
        pass
