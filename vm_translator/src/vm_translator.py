import argparse
from pathlib import Path

from parser import Parser
from code_writer import CodeWriter

def use_parser(input_path: Path, out_dir: Path):
    print("using parser")
    vm_parser = Parser(input_path)
    code_writer = CodeWriter(input_vm_path=input_path, out_dir=out_dir)
    while vm_parser.has_more_commands():
        vm_parser.advance()
        vm_cmd = vm_parser.command_type()
        if vm_cmd is None:
            raise ValueError("input vm command is None")
        code_writer.write_all_command(vm_cmd)
    code_writer.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    out_dir = Path("asm_files")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(input_path)
    if input_path.is_file():
        if input_path.suffix.lower() != ".vm":
            raise ValueError(f"Expected .vm file, but got {input_path}")
        use_parser(input_path, out_dir)
    
    elif input_path.is_dir():
        raise NotImplementedError

    else:
        raise ValueError