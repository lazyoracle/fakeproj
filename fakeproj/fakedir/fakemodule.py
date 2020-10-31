"""fake module with two fake functions used for tests
"""
import numpy as np
from typing import List
from typing import Iterable

Vector = List[float]


def fakefunc(fakelist: Vector) -> Iterable:
    """take a list and return numpy array

    Parameters
    ----------
    fakelist : list[float]
        list of ints

    Returns
    -------
    numpy.ndarray
        numpy array from python list
    """
    fake_array = np.array(fakelist)
    print(fake_array)
    return fake_array


def yaff(fakestr: str) -> str:
    """yet another fake function to print and return

    Parameters
    ----------
    fakestr : str
        any random string

    Returns
    -------
    str
        return the same string
    """
    print(fakestr)
    return fakestr
