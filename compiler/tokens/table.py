from . import Token, MACHINE_NAME, Store, ScopedName
from .helper import push, store, assign


class Index(Token):
    def setup(self, *args, **kwargs):
        self.value = args[0]
        self.index = args[1]

    def parse(self):
        return self.value + ";\n" + self.index + f";{MACHINE_NAME}.index();"


class DotIndex(Token):
    def setup(self, *args, **kwargs):
        self.value = args[0]
        self.index = args[1]

    def parse(self):
        return self.value + ";\n" + str(ScopedName([self.index])) + f";{MACHINE_NAME}.index();"


class AssignIndex(Token):
    def setup(self, *args, **kwargs):
        self.name = args[0]
        self.value = args[1]

    def parse(self):
        return self.value + ";\n" + self.name + assign()