import argparse
from pathlib import Path

from asm_encode import Code
from command_type import CommandKind
from parser import Parser
from symbol_table import SymbolTable

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(prog="Assembler")
    arg_parser.add_argument("-t", type=str, help="path to the input assembly file")
    args = arg_parser.parse_args()
    input_path = Path(args.t)

    parser = Parser(input_path)
    code = Code()

    # creat intermediate file
    # exclude blank line and spaces, and update symbol table
    symbol_table = SymbolTable()
    mid_path = input_path.parents[1] / "mid" / input_path.with_suffix(".txt").name
    mid_path.parent.mkdir(parents=True, exist_ok=True)
    with mid_path.open("w", encoding="utf-8") as f:
        ROM_line_counter = 0
        while parser.hasMoreCommands():
            command_type = parser.commandType()
            match command_type:
                case CommandKind.A_COMMAND | CommandKind.C_COMMAND:
                    f.write(f"{parser.get_latest_clean_command()}\n")
                    ROM_line_counter += 1
                case CommandKind.L_COMMAND:
                    symbol = parser.symbol()
                    try:
                        address = int(symbol)
                    except ValueError:
                        symbol_table.add_Entry(symbol, ROM_line_counter)
                case _:
                    raise ValueError(
                        f"encounterd an unexpected command type: {command_type}"
                    )
            parser.advance()

    # creat output file
    # replace all asm to bits
    parser = Parser(mid_path)
    out_path = input_path.parents[1] / "outputs" / input_path.with_suffix(".txt").name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        while parser.hasMoreCommands():
            command_type = parser.commandType()
            match command_type:
                case CommandKind.A_COMMAND:
                    symbol: str = parser.symbol()
                    try:
                        address = int(symbol)
                    except ValueError:
                        if not symbol_table.contains(symbol):
                            address = symbol_table.get_incr_new_address()
                            symbol_table.add_Entry(symbol, address)
                        else:
                            address = symbol_table.getAddress(symbol)
                    f.write("0" + f"{address:015b}" + "\n")
                case CommandKind.C_COMMAND:
                    f.write(
                        "111"
                        + str(code.comp(parser.comp()))
                        + str(code.dest(parser.dest()))
                        + str(code.jump(parser.jump()))
                        + "\n"
                    )
                case CommandKind.L_COMMAND:
                    pass
                case _:
                    pass
            parser.advance()
