from . import Token, Function, Call, ScopedName
from .helper import push, store, load




class ObjectSuite(Token):
    def __init__(self, *args, **kwargs):
        self.setup(*args[0], **kwargs)

    def setup(self, *args, **kwargs):
        self.statements = args

    def parse(self):
        result = ""

        for stmt in self.statements:
            result += str(stmt) + '\n'

        return result



class Object(Token):
    def __init__(self, *args, **kwargs):
        self.setup(*args[0], **kwargs)

    def setup(self, *args, **kwargs):
        self.name = args[0]
        self.suite = args[1]
    
    def parse(self):
        properties = []
        for prop in self.suite.statements:
            if isinstance(prop, Function):
                prop.set_owner(self.name)
                properties.append(prop)

        return str(Function([
            self.name,
            Call([load(ScopedName(["Table"]))]),
            store(ScopedName(["self"]))
        ] + list(map(str, properties)) + [load(ScopedName(["self"]))]))