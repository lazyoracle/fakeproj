"""module for testing get_ssh()
"""

from fakeproj.gooddir.sysmodule import get_ssh
import pytest
import os
import platform


@pytest.mark.unit
@pytest.mark.sysmodule
@pytest.mark.skipif(platform.system() == "Windows", reason="fails on Windows")
def test_get_ssh_linux(monkeypatch) -> None:
    """test get_ssh on Linux

    Parameters
    ----------
    monkeypatch : MonkeyPatch
        set os.environ['Home'] to a fixed value
    """
    monkeypatch.setitem(os.environ, "HOME", "/Baker/Street/221B")
    assert get_ssh() == "/Baker/Street/221B/.ssh"


@pytest.mark.unit
@pytest.mark.sysmodule
@pytest.mark.skipif(
    platform.system() == "Linux" or platform.system() == "Darwin",
    reason="fails on Linux/macOS",
)
def test_get_ssh_windows(monkeypatch) -> None:
    """test get_ssh on Windows

    Parameters
    ----------
    monkeypatch : MonkeyPatch
        set os.environ['Home'] to a fixed value
    """
    monkeypatch.setitem(os.environ, "HOME", "C:\\You\\In\\A\\While")
    assert get_ssh() == "C:\\You\\In\\A\\While\\.ssh"
