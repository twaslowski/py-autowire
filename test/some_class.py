from pyautowire import Injectable


class A(Injectable):
    field: str

    def __init__(self, field: str = "some-value"):
        super().__init__()
        self.field = field
