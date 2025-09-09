import argparse
from pathlib import Path

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

if __name__ == "__main__":
    # p = Path('/Users/masaki/Develop/learn/nand_to_tetris/assembler/test/inputs/plain_1.txt')
    arg_parser = argparse.ArgumentParser(prog="Assembler")
    arg_parser.add_argument('-t')
    args = arg_parser.parse_args()
    input_path = Path(args.t)

    parser = Parser(input_path)
    code = Code()

    # 中間ファイルの生成
    symbol_table = SymbolTable()
    mid_path = input_path.parents[1] / "mid" / input_path.with_suffix(".txt").name
    mid_path.parent.mkdir(parents=True, exist_ok=True)
    with mid_path.open("w", encoding="utf-8") as f:
        ROM_line_counter = 0
        while parser.hasMoreCommands():
            command_type = parser.commandType()
            match command_type:
                case "A_COMMAND":
                    symbol = parser.symbol()
                    try:
                        address = int(symbol)
                    except ValueError:
                        if not symbol_table.contains(symbol):
                            address = symbol_table.get_incr_new_address()
                            symbol_table.add_Entry(symbol, address)
                    
                    f.write(f"{parser.get_latest_clean_command()}\n")
                    ROM_line_counter += 1
                case "C_COMMAND":
                    f.write(f"{parser.get_latest_clean_command()}\n")
                    ROM_line_counter += 1
                case "L_COMMAND":
                    symbol = parser.symbol()
                    try:
                        address = int(symbol)
                    except ValueError:
                        symbol_table.add_Entry(symbol, ROM_line_counter) # @Xxxが初出でも、(Xxx)があれば、シンボルテーブルのアドレスを上書きする。
                case _:
                    pass
            parser.advance()

    parser = Parser(mid_path)
    out_path = input_path.parents[1] / "outputs" / input_path.with_suffix(".txt").name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        while parser.hasMoreCommands():
            command_type = parser.commandType()
            match command_type:
                case "A_COMMAND":
                    symbol: str = parser.symbol()
                    try:
                        address = int(symbol)
                    except ValueError:
                        if symbol_table.contains(symbol):
                            address = symbol_table.getAddress(symbol)
                        else:
                            raise ValueError()
                    f.write("0" + f"{address:015b}" + "\n")
                case "C_COMMAND":
                    f.write('111' + str(code.comp(parser.comp())) + str(code.dest(parser.dest())) + str(code.jump(parser.jump())) + "\n")
                case "L_COMMAND":
                    pass
                case _:
                    pass
            parser.advance()
