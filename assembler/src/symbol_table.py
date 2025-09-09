from predefined_symbols import PREDEFINED_SYMBOL_DICT, FREE_RAM_START_ADDRESS


class SymbolTable:
    def __init__(self) -> None:
        self.symbol_table: dict[str, int] = PREDEFINED_SYMBOL_DICT
        self.next_new_address: int = FREE_RAM_START_ADDRESS

    def add_Entry(self, symbol: str, address: int) -> None:
        self.symbol_table[symbol] = address

    def contains(self, symbol: str) -> bool:
        return symbol in self.symbol_table

    def getAddress(self, symbol: str) -> int:
        return self.symbol_table[symbol]

    def get_incr_new_address(self) -> int:
        addr = self.next_new_address
        self.next_new_address += 1
        return addr
