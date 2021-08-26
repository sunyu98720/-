import time
from functools import wraps
from seldom.logging import log


class Execute_time(object):
    def __init__(self):
        self.start_time = time.time()

    def __call__(self, func):
        @wraps(func)
        def time_dif(*args, **kwargs):
            self.test_demo()
            func()
            print(func.__name__, "执行时间为:", time.time() - self.start_time)
            return func(*args, **kwargs)

        return time_dif
