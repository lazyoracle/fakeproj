"""
module to test yet another fake functions
"""
import pytest
from fakeproj.fakedir.fakemodule import yaff


@pytest.mark.unit
@pytest.mark.fakemodule
def test_yaff() -> None:
    """test yaff"""
    assert yaff("foo") == "foo"
