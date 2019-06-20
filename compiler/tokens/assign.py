from . import Token, Identifier, MACHINE_NAME
from .helper import store, assign


class Assign(Token):
    def setup(self, *args, **kwargs):
        self.name = args[0]
        self.value = args[1]

    def parse(self):
        return self.value + f"{MACHINE_NAME}.clone();"+ self.name