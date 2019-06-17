from .token import Token
from .helper import push


class Value(Token):
    def setup(self, *args, **kwargs):
        self.value = str(args[0])

    def parse(self):
        return self.value