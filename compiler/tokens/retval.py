from .token import Token
from .helper import push


class Return(Token):
    def setup(self, *args, **kwargs):
        self.values = args

    def parse(self):
        result = ""

        for stmt in self.values:
            result += str(stmt) + '\n'

        return result