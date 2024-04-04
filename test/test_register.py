from pyautowire import autowire
from some_class import SomeClass


def test_trivial_autowiring():
    SomeClass().register()

    @autowire("some_class")
    def test_func(some_class: SomeClass):
        return some_class.field

    assert test_func() == "some-value"


def test_autowiring_with_args():
    SomeClass().register()

    @autowire("some_class")
    def test_func(string: str, some_class: SomeClass):
        return some_class.field + string

    assert test_func("arg") == "some-valuearg"
