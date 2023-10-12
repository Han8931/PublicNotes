import logging
from math import sqrt
from time import perf_counter
from typing import Any, Callable
import functools


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number) + 1)):
        if number % element == 0:
            return False
    return True


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args:Any, **kwargs:Any)->Any:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f"Execution of {func.__name__} took {run_time:.2f} seconds."
        )
        return value
    return wrapper

def with_logging(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args:Any, **kwargs:Any)->Any:
        logging.info(f"Calling {func.__name__}")
        value = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return value
    return wrapper


@with_logging
@benchmark
def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count



# class LoggingDecorator(AbstractDecorator):
#     def execute(self, upper_bound: int) -> int:
#         logging.info(f"Calling {self._decorated.__class__.__name__}")
#         value = self._decorated.execute(upper_bound)
#         logging.info(f"Finished {self._decorated.__class__.__name__}")
#         return value


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    # wrapper = benchmark(count_prime_numbers)
    # value = wrapper(1000)
    value = count_prime_numbers(10000)
    logging.info(f"Number of Primes: {value}")
    # return component.execute(50000)


if __name__ == "__main__":
    # out = main()
    # print(out)
    main()
