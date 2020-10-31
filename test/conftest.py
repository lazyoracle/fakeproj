"""conftest.py for unit testing
"""
import pytest
from typing import List

Vector = List[float]


@pytest.fixture()
def data_sample_list() -> Vector:
    """return sample list

    Returns
    -------
    list[float]
        [1, 2, 4]
    """
    return [1, 2, 4]
