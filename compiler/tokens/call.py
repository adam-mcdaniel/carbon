from . import Token, MACHINE_NAME
from .helper import push, store


class Arguments(Token):
    def setup(self, *args, **kwargs):
        # self.statements = args
        self.parameters = args[::-1]

    def parse(self):
        result = ""
        for param in self.parameters:
            result += param
        return result


class Call(Token):
    def setup(self, *args):
        self.values = args[::-1]
    
    def parse(self):
        newline = '\n'
        result = ''
        for value in self.values:
            result += value
        return result + f"{MACHINE_NAME}.call();"