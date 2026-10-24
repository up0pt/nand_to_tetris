from pathlib import Path
from textwrap import dedent

from jack_tokenizer import JackTokenizer

class CompilationEngine():
    def __init__(self, input_path: Path, output_path: Path) -> None:
        self.output_path: Path = output_path
        self.jack_tokenizer: JackTokenizer = JackTokenizer(input_path)

    def start(self) -> None:
        """
        Not listed on the textbook
        """
        raise NotImplementedError()
    
    def compile_class(self) -> None:
        self.jack_tokenizer.advance()
        keyword = self.jack_tokenizer.keyword()
        self.jack_tokenizer.advance()
        identifier = self.jack_tokenizer.identifier()


        self.output_path.write_text(
            dedent(
            f"""\
                <class>
                    <keyword> {keyword} </keyword>
                    <identifier> {identifier} </identifier>
                </class>"""), "utf-8"
            )

    def compile_class_var_dec(self) -> None:
        raise NotImplementedError()

    def compile_subroutine(self) -> None:
        raise NotImplementedError()

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