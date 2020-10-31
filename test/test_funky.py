"""module for testing funky_sum
"""
from test.conftest import data_sample_list  # noqa F401
from fakeproj.gooddir.goodmodule import funky_sum


def test_funky(data_sample_list) -> None:  # noqa F811
    """test funky sum with [1, 2, 4]"""
    assert funky_sum(data_sample_list) == 49
