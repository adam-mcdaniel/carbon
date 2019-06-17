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


class MethodCall(Token):
    def __init__(self, *args, **kwargs):
        self.setup(*args[0], **kwargs)

    def setup(self, *args):
        self.index_name = args[0].value
        self.owner = args[0]
        self.values = args[1:][::-1]
    
    def parse(self):
        return str(Call([self.owner, self.index_name] + list(self.values)))
        # newline = '\n'
        # result = ''
        # for value in self.values:
        #     result += value
        # return result + f"{MACHINE_NAME}.call();"