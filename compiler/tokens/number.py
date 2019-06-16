from .token import Token


class Number(Token):
    def setup(self, *args, **kwargs):
        self.value = str(*args[0])

    def parse(self):
        return "NUM " + str(self.value)