"""
module to test yet another fake functions
"""

from fakeproj.fakedir.fakemodule import yaff


def test_yaff() -> None:
    """test yaff"""
    assert yaff("foo") == "foo"
