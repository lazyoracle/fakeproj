"""Integration testing for pytha_quad function
"""

import pytest
from typing import List
from fakeproj.gooddir.goodmodule import pytha_quad
from fakeproj.fakedir.fakemodule import fakefunc


@pytest.mark.goodmodule
@pytest.mark.integration
@pytest.mark.parametrize(
    "numbers",
    [
        [1, 2, 2, 3],
        [2, 3, 6, 7],
        [6, 6, 7, 11],
        [2, 6, 9, 11],
    ],
)
def test_pytha_quad_integ(numbers: List[int]) -> None:
    """Integration Pass Test for pytha_quad

    Parameters
    ----------
    numbers : List[int]
        set of 4 numbers
    """
    np_numbers = fakefunc(numbers)
    list_numbers = np_numbers.tolist()
    assert list_numbers == numbers
    assert pytha_quad(list_numbers)
