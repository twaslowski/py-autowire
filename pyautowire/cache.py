from kink import di

from .injectable import Injectable


def register(injectable: Injectable):
    di[injectable.get_fully_qualified_name()] = injectable


def clear():
    di._services = {}
