from .token import Token


class String(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
