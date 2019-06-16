from .token import Token
from .helper import store

class Parameters(Token):
    def setup(self, *args, **kwargs):
        # self.statements = args
        self.parameters = args

    def parse(self):
        result = ""
        for param in self.parameters:
            result += store(param)
        return result