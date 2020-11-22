import fakeproj


class BechmarkSuite:

    params = ([0.1, 0.5, 1], [5, 10, 50])
    param_names = ["wait_time", "num_elements"]

    def setup(self, wait_time: float, num_elements: int) -> None:
        self.small_dict = dict(zip([range(1, 10, 1)], [range(100, 1000, 100)]))
        self.slow_obj = fakeproj.slowdir.slowmodule.SlowStuff(  # type: ignore
            wait_time, num_elements
        )

    def time_slow_list(self) -> None:
        self.slow_obj.slow_list()

    def time_slow_dict(self) -> None:
        self.slow_obj.slow_dict()

    def time_setup_dict(self) -> None:
        self.slow_obj.dict_setup()

    def mem_SlowStuff(self) -> None:
        fakeproj.slowdir.slowmodule.SlowStuff(0.1, 1000000)  # type: ignore
