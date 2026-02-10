from pathlib import Path
from typing import TextIO

from commands.command_kind import VmCmd

class CodeWriter:
    def __init__(self, input_vm_path: Path, out_dir: Path) -> None:
        self.path: Path = input_vm_path
        self.set_file_name(input_vm_path.stem)
        self.out_dir: Path = out_dir

        self._f: TextIO = open(self.out_dir / self.path.with_suffix(".asm"), "w", encoding="utf-8", newline="\n")
        self.label_id_num = 0

    def set_file_name(self, filename: str) -> None:
        self.file_name = filename

    def write_arithmetic(self, command: VmCmd) -> None:
        self.write_all_command(command)

    def write_push_pop(self, command: VmCmd) -> None:
        self.write_all_command(command)

    def write_all_command(self, command: VmCmd) -> None:
        self.label_id_num += 1
        self._f.write(command.asm_lines(str(self.label_id_num), self.file_name))

    def close(self) -> None:
        self._f.close