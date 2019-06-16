
from tokens import *
from lark import Lark, Transformer, UnexpectedCharacters, UnexpectedToken


class Parser(Transformer):
    function = Function
    collection = List
    table = Table
    object = Object
    number = Number
    string = String
    start = lambda s, tokens: "\n".join(map(str, tokens))


def parse(text):
    try:
        lexer = Lark.open(
            'grammar.lark',
            start='start',
            parser='lalr',
            lexer='standard'
        ).parse(text)
        
        return Parser().transform(lexer)

    except UnexpectedCharacters as e:
        newline = "\n"
        print(f"Unexpected characters on line {e.line}, column {e.column}:\n\t'{str(e).split(newline)[2]}'\n\t {str(e).split(newline)[3]}")

    return ""