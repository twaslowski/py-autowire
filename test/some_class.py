from context.autowire import Injectable


class SomeClass(Injectable):
    field: str

    def __init__(self, field: str = "some-value"):
        super().__init__()
        self.field = field
