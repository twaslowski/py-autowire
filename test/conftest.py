import pytest
from pyautowire.cache import clear


@pytest.fixture(autouse=True)
def clean_cache():
    # After every test, clean the cache
    yield
    clear()
