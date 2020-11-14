"""
module to test fake functions
"""

from fakeproj.fakedir.fakemodule import fakefunc
import pytest


def dummyfunc() -> int:
    """dummy function to use module

    Returns
    -------
    int
        length of array
    """
    mylist = [1.0, 2.0, 3.0, 4.0, 5.0]
    myarray = fakefunc(mylist)
    return len(myarray)


@pytest.mark.fakemodule
def test_dummy_func() -> None:
    """test dummy_func()"""
    assert dummyfunc() == 5
