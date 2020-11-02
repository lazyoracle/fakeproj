"""library of functions for sys derived tasks
"""
import os


def get_new_path(dir_name: str) -> str:
    """return new path with dir name

    Parameters
    ----------
    dir_name : str
        name of new directory to be made

    Returns
    -------
    str
        path to new directory
    """
    cwd = os.getcwd()
    new_path = os.path.join(cwd, dir_name)
    return new_path


def get_ssh() -> str:
    """return path to .ssh directory

    Returns
    -------
    str
        path to .ssh
    """
    home_dir = os.environ["HOME"]
    ssh_dir = os.path.join(home_dir, ".ssh")
    return ssh_dir
