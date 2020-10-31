"""module for testing funky_sum
"""
from fakeproj.gooddir.goodmodule import funky_sum

def test_funky() -> None:
    """test funky sum with [1, 2, 4]
    """
    test_data = [1, 2, 4]
    assert funky_sum(test_data) == 49