import time

class Decorator_demo():
    def time_test(self,fn):
        start_time = time.time()
        fn()
        end_time = time.time() - start_time
        return end_time
