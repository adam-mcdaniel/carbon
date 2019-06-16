from .token import Token


class Function(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)