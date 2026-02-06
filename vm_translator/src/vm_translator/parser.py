from vm_translator.vm_command_type import VMCommandKind


class Parser:
    def __init__(self) -> None:
        raise NotImplementedError

    def has_more_commands(self) -> bool:
        raise NotImplementedError

    def advance(self) -> None:
        raise NotImplementedError

    def command_type(self) -> VMCommandKind:
        raise NotImplementedError

    def arg1(self) -> str:
        raise NotImplementedError

    def arg2(self) -> int:
        raise NotImplementedError