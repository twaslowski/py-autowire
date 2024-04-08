import pytest

from pyautowire import (
    cache,
    autowire,
)
from pyautowire.error import (
    ParameterNotInCacheError,
    ParameterNotInSignatureError,
    ParameterNotInjectableError,
)
from some_class import A


def test_exception_thrown_when_di_cache_is_empty():
    # the fact that there is no way of unregistering things may be problematic
    cache.clear()

    @autowire("some_class")
    def test_func(some_class: A):
        return some_class.field

    with pytest.raises(ParameterNotInCacheError):
        test_func()


def test_exception_thrown_on_argument_mismatch():
    A().register()

    @autowire("another_class")
    def test_func(some_class: A):
        return some_class.field

    with pytest.raises(ParameterNotInSignatureError):
        test_func()


def test_exception_thrown_when_non_injectable_is_requested():
    @autowire("non_injectable_class")
    def test_func(non_injectable_class: str):
        return non_injectable_class

    with pytest.raises(ParameterNotInjectableError):
        test_func()
