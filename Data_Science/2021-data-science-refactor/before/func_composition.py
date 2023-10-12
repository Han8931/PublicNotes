import functools
from typing import Callable

from numpy import result_type


ComposableFunction = Callable[[float], float]

def compose(*functions: ComposableFunction)->ComposableFunction:
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)

def addThree(x:float)->float:
    return x+3

def multiplyByTwo(x: float)->float:
    return x*2

def main():
    x = 12
    myfunc = compose(addThree, addThree, multiplyByTwo, multiplyByTwo)
    result = myfunc(x)
    print(f"Result: {x}") 

if __name__ == "__main__":
    main()

