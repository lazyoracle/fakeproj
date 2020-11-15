"""module for testing sysmodule library
"""

from fakeproj.gooddir.sysmodule import get_new_path
import pytest
import os
import platform


@pytest.mark.unit
@pytest.mark.sysmodule
@pytest.mark.skipif(platform.system() == "Windows", reason="fails on Windows")
def test_get_new_path_linux(monkeypatch) -> None:
    """test get_new_path on linux

    Parameters
    ----------
    monkeypatch : MonkeyPatch
        monkeypatch the os.getcwd()
    """

    def mock_getcwd() -> str:
        """always return a mock path "/beam/me/up"

        Returns
        -------
        str
            mock path
        """
        return "/beam/me/up"

    monkeypatch.setattr(os, "getcwd", mock_getcwd)
    assert get_new_path("scotty") == "/beam/me/up/scotty"


@pytest.mark.sysmodule
@pytest.mark.skipif(
    platform.system() == "Linux" or platform.system() == "Darwin",
    reason="fails on Linux/macOS",
)
def test_get_new_path_win(monkeypatch) -> None:
    """test get_new_path on Windows

    Parameters
    ----------
    monkeypatch : MonkeyPatch
        monkeypatch the os.getcwd()
    """

    def mock_getcwd() -> str:
        """always return a mock path "C:\\You\\Later"

        Returns
        -------
        str
            mock path
        """
        return "C:\\You\\Later"

    monkeypatch.setattr(os, "getcwd", mock_getcwd)
    assert get_new_path("Alligator") == "C:\\You\\Later\\Alligator"
