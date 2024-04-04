import logging


class Injectable:
    @classmethod
    def get_fully_qualified_name(cls) -> str:
        return f"{cls.__module__}.{cls.__name__}"

    def register(self):
        logging.info(f"Registering {self.get_fully_qualified_name()} as singleton.")
        # cache.register(self)
        return self

    def refresh(self):
        logging.info(f"Refreshing {self.get_fully_qualified_name()} instance.")
        # cache.register(self)
