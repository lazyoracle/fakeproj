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
    result = 0.0
    for i in numbers:
        if i != 0:
            result += 1.0 / i
    return result


def pytha_quad(numbers: List[int]) -> bool:
    """check if a list is pythagorean quadruplet

    Parameters
    ----------
    numbers : List[int]
        list of 4 numbers

    Returns
    -------
    bool
        if it is a pythagorean quadruplet
    """
    assert len(numbers) == 4, "Should be a list of 4 numbers"

    sq_numbers = [i * i for i in numbers[:-1]]
    return sum(sq_numbers) == (numbers[-1] * numbers[-1])

def palindrome(word: str) -> bool:
    """Check if the word is a palindrome

    Parameters
    ----------
    word : str
        word to check

    Returns
    -------
    bool
        whether it is palindrome or not
    """
    return word == word[::-1]