from . import Token, MACHINE_NAME
from .helper import push, store, load


class List(Token):
    def setup(self, *args, **kwargs):
        self.values = args[::-1]
        self.length = len(self.values)
    
    def parse(self):
        return '\n'.join(self.values) + push(f"Object::Number({self.length})") + push("Object::String(\"std::List\")") + f";{MACHINE_NAME}.load(); {MACHINE_NAME}.call();" 