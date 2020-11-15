"""module for testing reciprocal sum
"""
import pytest
from test.conftest import data_sample_list  # noqa F401
from fakeproj.gooddir.goodmodule import recp_sum


@pytest.mark.unit
@pytest.mark.goodmodule
def test_recp(data_sample_list) -> None:  # noqa F811
    """test reciprocal sum on [1, 2, 4]"""
    assert recp_sum(data_sample_list) == 1.75
