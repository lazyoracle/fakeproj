"""module for testing reciprocal sum
"""

from fakeproj.gooddir.goodmodule import recp_sum

def test_recp() -> None:
    test_data = [1, 2, 4]
    assert recp_sum(test_data) == 1.75

print(recp_sum([1, 2, 4]))