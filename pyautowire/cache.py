from kink import di

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyautowire.injectable import Injectable


def register(injectable: "Injectable") -> "Injectable":
    di[injectable.get_fully_qualified_name()] = injectable
    return injectable


def clear() -> None:
    di._services = {}
