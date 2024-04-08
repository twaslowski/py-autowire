import pytest

from pyautowire import autowire
from pyautowire.error import ParameterNotInCacheError
from some_class import A


class B(A):
    pass


def test_match_by_alias():
    B().register(alias="a")

    @autowire("a")
    def func(a: A):
        return a

    assert func().field == "some-value"


def test_cache_miss_by_alias():
    B().register(alias="c")

    @autowire("a")
    def func(a: A):
        return a

    with pytest.raises(ParameterNotInCacheError):
        func()
