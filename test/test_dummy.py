"""
module to test fake functions
"""

from fakeproj.fakedir.fakemodule import fakefunc


def dummyfunc() -> int:
    """dummy function to use module

    Returns
    -------
    int
        length of array
    """
    mylist = [1, 2, 3, 4, 5]
    myarray = fakefunc(mylist)
    return len(myarray)


def test_dummy_func() -> None:
    """test dummy_func()"""
    assert dummyfunc() == 5
