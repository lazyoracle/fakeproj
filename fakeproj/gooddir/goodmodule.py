"""Functions attempting to do borderline useful stuff
"""

def funky_sum(numbers: list) -> float:
    """return the sum of a list offset by 42

    Parameters
    ----------
    numbers : list[float]
        list of numbers

    Returns
    -------
    float
        sum offset by 42
    """
    return sum(numbers) + 42

def recp_sum(numbers: list) -> float:
    """calculate reciprocal sum of a list of numbers

    Parameters
    ----------
    numbers : list[float]
        list of numbers

    Returns
    -------
    float
        reciprocal sum
    """
    result = 0
    for i in numbers:
        if i != 0:
            result += 1.0/i
    return result