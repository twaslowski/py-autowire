from pyautowire import autowire
from some_class import A


def test_kwargs_are_not_overwritten_if_provided():
    @autowire("some_class")
    def test_func(some_class: A):
        return some_class.field

    A().register()
    assert test_func(some_class=A(field="new-value")) == "new-value"
