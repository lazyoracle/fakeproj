"""
module to test fake functions
"""

from fakeproj.fakedir.fakemodule import fakefunc
import pytest


@pytest.mark.unit
@pytest.mark.fakemodule
def test_dummy_func() -> None:
    """test dummy_func()"""
    mylist = [1, 2, 3, 4, 5]
    assert fakefunc(mylist).tolist() == mylist
