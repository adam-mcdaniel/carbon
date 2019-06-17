from . import Token, String
from .helper import load, store, push


class Identifier(Token):
    def setup(self, *args, **kwargs):
        self.value = str(args[0])

    def parse(self):
        return self.value


class ScopedName(Token):
    def setup(self, *args, **kwargs):
        self.names = args

    def parse(self):
        return str(String([f"\"{'::'.join(self.names)}\""]))


class Load(Token):
    def setup(self, *args, **kwargs):
        self.name = str(args[0])

    def parse(self):
        return load(self.name)


class Store(Token):
    def setup(self, *args, **kwargs):
        self.name = str(args[0])

    def parse(self):
        return store(self.name)
