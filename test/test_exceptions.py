import pytest

from pyautowire import (
    cache,
    autowire,
    ParameterNotInCacheError,
    ParameterNotInSignatureError,
)
from some_class import SomeClass


def test_exception_thrown_when_di_cache_is_empty():
    # the fact that there is no way of unregistering things may be problematic
    cache.clear()

    @autowire("some_class")
    def test_func(some_class: SomeClass):
        return some_class.field

    with pytest.raises(ParameterNotInCacheError):
        test_func()


def test_exception_thrown_on_argument_mismatch():
    SomeClass().register()

    @autowire("another_class")
    def test_func(some_class: SomeClass):
        return some_class.field

    with pytest.raises(ParameterNotInSignatureError):
        test_func()
