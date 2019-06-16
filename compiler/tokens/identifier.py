from .token import Token


class Identifier(Token):
    def setup(self, *args, **kwargs):
        self.value = str(args[0])

    def parse(self):
        return "IDENT " + str(self.value)