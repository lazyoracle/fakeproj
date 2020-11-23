"""sample benchmark implementation
"""
from fakeproj.slowdir.slowmodule import SlowStuff


class BechmarkSuite:
    """Timing and Memory Benchmark Suite for SlowStuff"""

    params = ([0.01, 0.1], [5, 500000])
    param_names = ["wait_time", "num_elements"]

    def setup(self, wait_time: float, num_elements: int) -> None:
        """setup function for BenchmarkSuite

        Parameters
        ----------
        wait_time : float
            time to wait between iterations
        num_elements : int
            number of elements in iterables
        """
        self.small_dict = dict(zip([range(1, 10, 1)], [range(100, 1000, 100)]))
        self.slow_obj = SlowStuff(wait_time, num_elements)

    def time_slow_list(self, wait_time, num_elements) -> None:
        """timing benchmark for slow_list()

        Parameters
        ----------
        wait_time : float
            time to wait between iterations
        num_elements : int
            number of elements in iterables
        """
        self.slow_obj.slow_list()

    def time_slow_dict(self, wait_time, num_elements) -> None:
        """timing benchmark for slow_dict()

        Parameters
        ----------
        wait_time : float
            time to wait between iterations
        num_elements : int
            number of elements in iterables
        """
        self.slow_obj.slow_dict()

    def time_setup_dict(self, wait_time, num_elements) -> None:
        """timing benchmark for setup_dict()

        Parameters
        ----------
        wait_time : float
            time to wait between iterations
        num_elements : int
            number of elements in iterables
        """
        self.slow_obj.dict_setup(self.small_dict)

    def mem_SlowStuff(self, wait_time, num_elements) -> SlowStuff:
        """memory benchmark for SlowStuff

        Parameters
        ----------
        wait_time : float
            time to wait between iterations
        num_elements : int
            number of elements in iterables

        Returns
        -------
        SlowStuff
            SlowStuff object
        """
        big_slow_obj = SlowStuff(wait_time, num_elements)  # type: ignore
        return big_slow_obj
