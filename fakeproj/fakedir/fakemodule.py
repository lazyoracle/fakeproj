"""fake module with fake functions used for tests
"""
import numpy as np


def fakefunc(fakelist: list):
    """take a list and return numpy array

    Parameters
    ----------
    fakelist : list
        list of ints

    Returns
    -------
    numpy.ndarray
        numpy array from python list
    """
    fake_array = np.array(fakelist)
    print(fake_array)
    return fake_array


def yaff(fakestr: str):
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

def complexfunc(fakelist: list) -> int:
    """Complex function with if-elif and list comp

    Parameters
    ----------
    fakelist : list
        list of ints

    Returns
    -------
    int
        length of comprehended list
    """
    try:
        if len(fakelist) == 1:
            print('1')
            
        elif len(fakelist) == 2:
            print('2')
            
        elif len(fakelist) == 3:
            print('3')
            
        elif len(fakelist) == 4:
            print('4')
            
        elif len(fakelist) == 5:
            print('5')
            
        elif len(fakelist) == 6:
            print('6')
            
        elif len(fakelist) == 7:
            print('7')
            
        elif len(fakelist) == 8:
            print('8')
            
        elif len(fakelist) == 9:
            print('9')
            
        elif len(fakelist) == 10:
            print('10')
            
        elif len(fakelist) == 11:
            print('11')
        else:
            return 42
    except KeyboardInterrupt:
        pass
    except ArithmeticError:
        pass
    except FloatingPointError:
        pass

    new_list = [ i*i for i in fakelist]

    return len(new_list)

