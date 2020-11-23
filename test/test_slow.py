"""Test SlowStuff methods
"""

import pytest
from fakeproj.slowdir.slowmodule import SlowStuff


@pytest.mark.unit
@pytest.mark.slow
@pytest.mark.parametrize(
    "wait_time",
    [0.5, 1.0],
)
@pytest.mark.parametrize(
    "num_elements",
    [2, 5],
)
@pytest.mark.parametrize(
    "small_dict",
    [{"A": 1, "B": 2, "C": 3}, dict(zip([range(1, 10, 1)], [range(100, 1000, 100)]))],
)
def test_SlowStuff(wait_time: float, num_elements: int, small_dict: dict) -> None:
    """test the 3 methods of SlowStuff class

    Parameters
    ----------
    wait_time : float
        time to wait between iterations
    num_elements : int
        number of elements in iterables
    small_dict : dict
        pre-made sample dictionary
    """
    slow_obj = SlowStuff(0.5, 10)

    assert slow_obj.slow_dict()
    assert slow_obj.slow_list()
    assert slow_obj.dict_setup(small_dict)
