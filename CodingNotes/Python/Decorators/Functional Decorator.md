
# Functional Decorators

A very naive approach to benchmark the `count_prime_numbers` is the following way:
```python
import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number) + 1)):
        if number % element == 0:
            return False
    return True

def count_prime_numbers(upper_bound: int) -> int:

    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count


def benchmark(upper_bound: int) -> int:
    start_time = perf_counter()
    value = count_prime_numbers(upper_bound)
    end_time = perf_counter()
    run_time = end_time - start_time
    logging.info(
        f"Execution of count_prime_numbers took {run_time:.2f} seconds."
    )
    return value

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = benchmark(100000)
    logging.info(f"Number of Primes: {value}")

if __name__ == "__main__":
    # out = main()
    # print(out)
    main()

```

However, the benchmark function takes the `count_prime_numbers ` directly so I cannot benchmark other functions. To make the function more generic, 

```python
def benchmark(func: Callable[[int], int]) -> int:
    start_time = perf_counter()
    value = func(upper_bound)
    end_time = perf_counter()
    run_time = end_time - start_time
    logging.info(
        f"Execution of count_prime_numbers took {run_time:.2f} seconds."
    )
    return value
```
However, we still need to specify the `upper_bound `, so

```python
def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
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
```

To run it, 

```python
def main() -> None:
    logging.basicConfig(level=logging.INFO)
    wrapper = benchmark(count_prime_numbers)
	value = wrapper(100)
    logging.info(f"Number of Primes: {value}")
```

For logging, we can create a logger wrapper:

```python
def with_logging(func: Callable[..., Any]) -> Callable[..., Any]:
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

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = count_prime_numbers(10000)
    logging.info(f"Number of Primes: {value}")
```

## Functools

If you run the above code, it will log with a function name `wrapper`, but this is not what we want. 

```python
import functools
@functools.wraps(func)
```
Put that line above wrappers. 

## Decorator with Arguments

```python

def with_logging(logger: logger.Logger):
	def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
	    def wrapper(*args:Any, **kwargs:Any)->Any:
	        logger.info(f"Calling {func.__name__}")
	        value = func(*args, **kwargs)
	        logger.info(f"Finished {func.__name__}")
	        return value
	    return wrapper
	return decorator

logger = logging.getLogger("my_app")

@with_logging(logger)
@benchmark 
def count_prime_numbers():
	...
```

There is another approach to do the same job using `partial`:
```python
with_default_logging = functools.partial(with_logging, logger=logger)

@with_default_logging() 
@benchmark 
def count_prime_numbers():
	...
```
- Note that we need to put parenthesis when we call the partial function as it is a function.

To further simplify the code:
```python

def with_logging(func: Callable[..., Any], logger: logging.Logger) -> Callable[..., Any]:
	def wrapper(*args:Any, **kwargs:Any)->Any:
		logger.info(f"Calling {func.__name__}")
		value = func(*args, **kwargs)
		logger.info(f"Finished {func.__name__}")
		return value
	return wrapper

with_default_logging = functools.partial(with_logging, logger=logger)

@with_default_logging
@benchmark 
def count_prime_numbers():
	...
```


