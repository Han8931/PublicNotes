[Reference](https://youtu.be/ph2HjBQuI8Y)
## Replacing Class Structure by Functions

Functions can often replace classes. 
```python
from typing import Callable 
`TradingStrategyPattern = Callable[[list[int]], bool]`

def should_buy(prices: list[int])->bool:
	return prices[-1]<32_000

@dataclass
class TradingBot:
	buy_strategy: TradingStrategyPattern 

	def do_some_action(self,):
		self.buy_strategy.should_buy

bot = TradingBot(should_buy)
```

```python
from typing import Callable 

def apply_func(a:int, b:int, func: Callable[[int, int], float]):
	return func(a, b)

def divide(a:int, b:int)->float:
	return a/b

apply_func(1,2,divide)
```

## Passing Extra Arguments Using Closures 

```python
def should_buy(prices: list[int])->bool:
	return prices[-1]<32_000
```

Here we cannot pass the window size parameter, so we can use a closure to pass a parameter. 

```python
def should_buy_closure(window_size: int)->TradingStrategyPattern:
	def should_buy(prices: list[int])->bool:
		return prices[window_size]<32_000
	return should_buy 
```

## Using Partial Functions

Partial functions allow us to fix a certain number of arguments of a function and generate a new function.

Let's say we have a function that computes the power of a base number:

```python
def power(base, exp):
	return base**exp
```

Then, we want to create another function that is dedicated to compute square. It is tempting to create a function like
```python
def square(base):
	return base**2
```

You can utilize a partial function in python to do the same thing

```python
from functools import partial

square = partial(power, 2)
```