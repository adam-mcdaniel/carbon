from . import Token, MACHINE_NAME, Store, ScopedName, AssignIndex, Index
from .helper import push, store, load


class Parameters(Token):
    def setup(self, *args, **kwargs):
        self.parameters = args

    def parse(self):
        result = ""
        for param in self.parameters:
            result += str(Store([ScopedName([param])]))
        return result


class Function(Token):
    def setup(self, *args):
        self.owner = None
        self.statements = args
    
    def set_owner(self, name):
        self.owner = name

    def parse(self):
        newline = '\n'
        result = push(f"Object::Fn(Fn([](Machine& {MACHINE_NAME}) {{{newline.join(self.statements[1:])}}}, {MACHINE_NAME}))")
        
        if self.owner:
            result = str(AssignIndex([Index([load(ScopedName(["self"])), self.statements[0]]), result]))
        else:
            result += store(self.statements[0])

        return result


class LambdaFunction(Token):
    def setup(self, *args):
        self.statements = args

    def parse(self):
        newline = '\n'
        return push(f"Object::Fn(Fn([](Machine& {MACHINE_NAME}) {{{self.statements[0]};{newline.join(self.statements[1:])}}}, {MACHINE_NAME}))")