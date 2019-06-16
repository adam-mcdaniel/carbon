from .token import Token


class Suite(Token):
    def setup(self, *args, **kwargs):
        self.statements = args

    def parse(self):
        result = ""

        for stmt in self.statements:
            result += str(stmt) + '\n'

        return result