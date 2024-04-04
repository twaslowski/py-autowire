from pyautowire import autowire
from some_class import SomeClass


def test_cache_object_can_be_overwritten():
    @autowire("some_class")
    def test_func(some_class: SomeClass):
        return some_class.field

    SomeClass("new-value").refresh()
    assert test_func() == "new-value"
