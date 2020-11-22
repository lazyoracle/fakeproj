"""Attempting to do things very slowly
"""

import time


class SlowStuff:
    """
    methods for doing things really slowly
    """

    def __init__(self, wait_time: float, num_elements: int) -> None:
        """Constructor for SlowStuff

        Parameters
        ----------
        wait_time : float
            seconds to wait between iteration steps
        num_elements : int
            number of elements in the iterable
        """
        self.wait_time = wait_time
        self.num_elements = num_elements

    def slow_list(self) -> bool:
        """create a list and iterate slowly

        Returns
        -------
        bool
            True if the iteration completes
        """
        big_list = [range(self.num_elements)]

        for ele in big_list:
            time.sleep(self.wait_time)

        return True

    def slow_dict(self) -> bool:
        """create a dictionary and iterate slowly

        Returns
        -------
        bool
            True if the iteration completes
        """
        list_1 = [range(1, self.num_elements, 1)]
        list_2 = [range(1000, self.num_elements, 100)]
        big_dict = dict(zip(list_1, list_2))

        for key, value in big_dict.items():
            time.sleep(self.wait_time)

        return True

    def dict_setup(self, pre_made_dict: dict) -> bool:
        """iterate slowly through the supplied dictionary

        Parameters
        ----------
        pre_made_dict : dict
            dictionary of random values

        Returns
        -------
        bool
            True if the iteration completes
        """
        for key, value in pre_made_dict.items():
            time.sleep(self.wait_time)

        return True
