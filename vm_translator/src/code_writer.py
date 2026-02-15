from pathlib import Path
from typing import TextIO

from commands.command_kind import VmCmd
from commands.function_call import Call

class CodeWriter:
    def __init__(self, input_vm_top_path: Path) -> None:
        self.input_vm_top_path: Path = input_vm_top_path
        self.output_file_path: Path = self.input_vm_top_path.with_suffix(".asm")

        self._f: TextIO = open(self.output_file_path, "w", encoding="utf-8", newline="\n")
        self.label_id_num = 0

        self.add_boostrap()
        print("write boostrap")
        print(f"output file is {self.output_file_path}")

    def add_boostrap(self) -> None:
        call_sysinit = Call("Sys.init", "0")
        self._f.write("""
@256
D=A
@SP
M=D
                    """+call_sysinit.asm_lines("SYS0", "Sys"))
    
    def get_output_file_path(self) -> Path:
        return self.output_file_path

    def set_file_name(self, vm_file_path: Path) -> None:
        self.reading_vm_file_path = vm_file_path

    def write_all_command(self, command: VmCmd) -> None:
        self.label_id_num += 1
        relative_path_to_reading_vm_file = self.reading_vm_file_path.relative_to(self.input_vm_top_path)
        self._f.write(command.asm_lines(str(self.label_id_num), ".".join(relative_path_to_reading_vm_file.with_suffix("").parts)))

    def close(self) -> None:
        self._f.close