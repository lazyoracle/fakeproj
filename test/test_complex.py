"""
module to test complex function
"""

from fakeproj.fakedir.fakemodule import complexfunc

def test_complex() -> None:
    """test complex function
    """
    test_list_1 = [1, 2, 3, 4, 5, 6, 7]
    test_list_2 = range(1, 15, 1)

    assert complexfunc(test_list_1) == len(test_list_1)
    assert complexfunc(test_list_2) == 42