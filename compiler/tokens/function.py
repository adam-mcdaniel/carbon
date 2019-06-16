from . import Token, MACHINE_NAME, Store, ScopedName
from .helper import push, store


class Parameters(Token):
    def setup(self, *args, **kwargs):
        # self.statements = args
        self.parameters = args

    def parse(self):
        result = ""
        for param in self.parameters:
            result += str(Store([ScopedName(param)]))
        return result


class Function(Token):
    def setup(self, *args):
        self.statements = args
    
    def parse(self):
        newline = '\n'
        result = push(f"Object::Fn([](Machine& {MACHINE_NAME}) {{{newline.join(self.statements[1:])}}})")
        result += store(self.statements[0])
        return result