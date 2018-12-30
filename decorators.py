import time
from functools import wraps


def timing(decorated):
    @wraps(decorated)
    def decorator(*args, **kwargs):
        print(f'Calling {decorated.__name__} function')
        start_time_time = time.time()
        start_time_perf = time.perf_counter()
        start_time_process = time.process_time()

        result = decorated(*args, **kwargs)

        float_digits = '.15f'
        end_time_time = time.time()
        end_time_perf = time.perf_counter()
        end_time_process = time.process_time()
        print(
            f'Time time:\t'
            f'{format(end_time_time - start_time_time, float_digits)} s'
        )
        print(
            f'Perf time:\t'
            f'{format(end_time_perf - start_time_perf, float_digits)} s'
        )
        print(
            f'Proc time:\t'
            f'{format(end_time_process - start_time_process, float_digits)} s'
        )
        return result
    return decorator
