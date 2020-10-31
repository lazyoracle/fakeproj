"""Functions attempting to do borderline useful stuff
"""
from typing import List

Vector = List[float]


def funky_sum(numbers: Vector) -> float:
    """return the sum of a list offset by 42

    Parameters
    ----------
    numbers : list[float]
        list of numbers

    Returns
    -------
    float
        sum offset by 42
    """
    return sum(numbers) + 42


def recp_sum(numbers: Vector) -> float:
    """calculate reciprocal sum of a list of numbers

    Parameters
    ----------
    numbers : list[float]
        list of numbers

    Returns
    -------
    float
        reciprocal sum
    """
    result = 0
    for i in numbers:
        if i != 0:
            result += 1.0 / i
    return result
