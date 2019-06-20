
from tokens import *
from lark import Lark, Transformer, UnexpectedCharacters, UnexpectedToken
from lark.indenter import Indenter as LarkIndentor


class Indenter(LarkIndentor):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


class Parser(Transformer):
    suite = Suite
    fn = Function
    collection = List
    store = Store
    index = Index
    dot_index = DotIndex
    assign_index = AssignIndex
    list = List
    load = Load
    object = Object
    object_suite = ObjectSuite
    method_call = MethodCall
    number = Number
    string = String
    name = ScopedName
    ident = Identifier
    value = Value
    call = Call
    arguments = Arguments
    assign = Assign
    retval = Return
    parameters = Parameters

    def true(a, b): return "Object::Bool(true)"

    def false(a, b): return "Object::Bool(false)"

    def start(_, tokens): return "\n".join(map(str, tokens))


kwargs = dict(postlex=Indenter())


def parse(text):
    try:
        lexer = Lark.open(
            'grammar.lark',
            start='start',
            parser='lalr',
            lexer='standard',
            **kwargs
        ).parse(text)

        return Parser().transform(lexer).replace(';;', ';').replace(';;', ';').replace('\t', '').replace('\n', '').replace(';', ';\n\t')

    except UnexpectedCharacters as e:
        newline = "\n"
        print(
            f"Unexpected characters on line {e.line}, column {e.column}:\n\t'{str(e).split(newline)[2]}'\n\t {str(e).split(newline)[3]}")

    except UnexpectedToken as e:
        newline = "\n"
        print(f'{str(e).split(newline)[0][:-1]}')

    return ""
