"""Module for testing palindrome function
"""

import pytest
from typing import Tuple
from fakeproj.gooddir.goodmodule import palindrome


@pytest.mark.unit
@pytest.mark.parametrize(
    "word_result",
    [("ABA", True), ("199", False), ("ABBA", True), ("ABCBA", True)],
)
def test_palindrome(word_result: Tuple[str, bool]) -> None:
    """Check palindrome function

    Parameters
    ----------
    word_result : Tuple[str, bool]
        word and expected result
    """
    word, result = word_result
    assert palindrome(word) == result