from kink import di


def register(injectable):
    di[injectable.get_fully_qualified_name()] = injectable


def clear():
    di._services = {}
