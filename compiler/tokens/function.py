from . import Token, MACHINE_NAME


class Function(Token):
    def setup(self, *args):
        self.statements = args
    
    def parse(self):
        newline = '\n'
        return f"{MACHINE_NAME}.push([](Machine& {MACHINE_NAME} {{{newline.join(self.statements)}}});"