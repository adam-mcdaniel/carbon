

class Token:
    def __init__(self, *args, **kwargs):
        self.setup(*list(map(str, args[0])), **kwargs)

    def setup(self, *args, **kwargs):
        pass

    def __str__(self): return self.parse()

    def parse(self):
        return ""