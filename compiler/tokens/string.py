from .token import Token
from .helper import push


class String(Token):
    def setup(self, *args, **kwargs):
        self.value = str(args[0])

    def parse(self): return push(f"Object::String({self.value})")
