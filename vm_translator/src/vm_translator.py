import argparse
from pathlib import Path

from parser import Parser
from code_writer import CodeWriter

def use_parser(input_vm_file: Path, code_writer: CodeWriter):
    vm_parser = Parser(input_vm_file)
    code_writer.set_file_name(input_vm_file)
    while vm_parser.has_more_commands():
        vm_parser.advance()
        vm_cmd = vm_parser.command_type()
        if vm_cmd is None:
            raise ValueError("input vm command is None")
        code_writer.write_all_command(vm_cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    out_dir = Path("asm_files").resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    code_writer = CodeWriter(input_vm_top_path=input_path)

    if input_path.is_file():
        if input_path.suffix.lower() != ".vm":
            raise ValueError(f"Expected .vm file, but got {input_path}")
        use_parser(input_path, code_writer)
        code_writer.close()
    
    elif input_path.is_dir():
        vm_file_paths = input_path.rglob('*.vm', case_sensitive=False) # match regardless case
        if not vm_file_paths:
            code_writer.close()
            raise ValueError("No vm files in the given folder!")
        for vm_file_path in vm_file_paths:
            use_parser(vm_file_path, code_writer)
        code_writer.close()

    else:
        code_writer.close()
        raise ValueError("Not found the file or directory")
