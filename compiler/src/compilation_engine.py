from pathlib import Path

from jack_tokenizer import JackTokenizer, TokenType

class CompilationEngine():
    def __init__(self, input_path: Path, output_path: Path) -> None:
        self.output_path: Path = output_path
        self.jack_tokenizer: JackTokenizer = JackTokenizer(input_path)
        self.jack_tokenizer.advance()

    def start(self) -> None:
        """
        Not listed on the textbook
        """
        raise NotImplementedError()
    
    def compile_class(self) -> None:
        compiled_xml_str = ""

        keyword = self.jack_tokenizer.keyword() #TODO:　そもそもkeywordでない場合のエラー
        if keyword != "class":
            raise SyntaxError(f'Expected "class" but got "{keyword}"')
        compiled_xml_str += "<class>\n<keyword> class </keyword>\n"
        self.jack_tokenizer.advance()

        identifier = self.jack_tokenizer.identifier() #TODO:　そもそもidentifierでない場合のエラー
        compiled_xml_str += f"<identifier> {identifier} </identifier>\n"
        self.jack_tokenizer.advance()

        left_brace = self.jack_tokenizer.symbol()
        compiled_xml_str += f"<symbol> {left_brace} </symbol>\n"
        self.jack_tokenizer.advance()

        while self.jack_tokenizer.get_token() in ("static", "field"):
            compiled_xml_str += self.compile_class_var_dec()

        while self.jack_tokenizer.get_token() in ("constructor", "function", "method"):
            raise NotImplementedError("Implement subroutine in progress")
            compiled_xml_str += self.compile_subroutine()

        right_brace = self.jack_tokenizer.symbol()
        compiled_xml_str += f"<symbol> {right_brace} </symbol>\n"
        self.jack_tokenizer.advance()
        
        compiled_xml_str += "</class>"
        self.output_path.write_text(compiled_xml_str, "utf-8")

    def compile_class_var_dec(self) -> str:
        compiled_xml_str = ""

        compiled_xml_str += "<classVarDec>\n"

        compiled_xml_str += f"<keyword> {self.jack_tokenizer.keyword()} </keyword>\n"
        self.jack_tokenizer.advance()

        if self.jack_tokenizer.get_token() in ("int", "char", "boolean"):
            compiled_xml_str += f"<keyword> {self.jack_tokenizer.keyword()} </keyword>\n"
            self.jack_tokenizer.advance()
        elif self.jack_tokenizer.token_type() == TokenType.IDENTIFIER:
            compiled_xml_str += f"<identifier> {self.jack_tokenizer.identifier()} </identifier>\n"
            self.jack_tokenizer.advance()
        else:
            raise SyntaxError(f"Expected int, char, boolean, or ClassName but got {self.jack_tokenizer.get_token()}")

        compiled_xml_str += f"<identifier> {self.jack_tokenizer.get_token()} </identifier>\n"
        self.jack_tokenizer.advance()

        while self.jack_tokenizer.get_token() == ",":
            compiled_xml_str += "<symbol> , </symbol>\n"
            self.jack_tokenizer.advance()
            if self.jack_tokenizer.token_type() != TokenType.IDENTIFIER:
                raise SyntaxError(f"Expected Identifier but got {self.jack_tokenizer.get_token()} (token type is {self.jack_tokenizer.token_type()})")
            compiled_xml_str += f"<identifier> {self.jack_tokenizer.get_token()} </identifier>\n"
            self.jack_tokenizer.advance()

        compiled_xml_str += "<symbol> ; </symbol>\n"
        self.jack_tokenizer.advance()

        compiled_xml_str += "</classVarDec>\n"
        
        return compiled_xml_str

    def compile_subroutine(self) -> str:
        return ""

    def compile_parameter_list(self) -> None:
        raise NotImplementedError()

    def compile_statements(self) -> None:
        raise NotImplementedError()

    def compile_do(self) -> None:
        raise NotImplementedError()

    def compile_let(self) -> None:
        raise NotImplementedError()

    def compile_while(self) -> None:
        raise NotImplementedError()

    def compile_return(self) -> None:
        raise NotImplementedError()

    def compile_if(self) -> None:
        raise NotImplementedError()

    def compile_expression(self) -> None:
        raise NotImplementedError()

    def compile_term(self) -> None:
        raise NotImplementedError()

    def compile_expression_list(self) -> None:
        raise NotImplementedError()