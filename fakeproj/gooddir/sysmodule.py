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
