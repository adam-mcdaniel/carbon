from .token import Token


class Number(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

