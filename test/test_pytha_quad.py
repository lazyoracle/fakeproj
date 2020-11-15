"""module for testing pythagorean quadruplets function
"""

import pytest
from fakeproj.gooddir.goodmodule import pytha_quad
from typing import List


@pytest.mark.unit
@pytest.mark.goodmodule
@pytest.mark.parametrize(
    "numbers",
    [
        [1, 2, 2, 3],
        [2, 3, 6, 7],
        [4, 4, 7, 9],
        [1, 4, 8, 9],
        [6, 6, 7, 11],
        [2, 6, 9, 11],
    ],
)
def test_pytha_quad(numbers: List[int]) -> None:
    """pass test for pythagorean quads

    Parameters
    ----------
    numbers : List[int]
        set of 4 numbers
    """
    assert pytha_quad(numbers)


@pytest.mark.unit
@pytest.mark.goodmodule
@pytest.mark.parametrize("numbers", [[1, 1, 1, 1], [1, 2, 3, 4], [5, 6, 7, 8]])
def test_not_pytha_quad(numbers: List[int]) -> None:
    """fail test for pythagorean quads

    Parameters
    ----------
    numbers : List[int]
        set of 4 numbers
    """
    assert not pytha_quad(numbers)
