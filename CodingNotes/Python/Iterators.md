# Introduction

An iterator is an object that is used to traverse through some sequence of items. In Python, it is an object that implements an iterator protocol which defines two dunder methods: 1) `__iter__` and 2) `__next__`.

You can create an iterator and print it by using `iter` and `next` functions. 
```python
def main()->None:
    countries = ("Germany", 'France', 'Italy', 'Spain', 'Portugal', 'Greece')
    country_iter = iter(countries)
    print(next(country_iter))
    print(next(country_iter))
    print(next(country_iter))

if __name__ == "__main__":
    main()

```

To print all countries, you can do as follows:
```python
    while True:
        try:
            country = next(country_iter)
        except StopIteration:
            break
        else:
            print(country)
```

```python
    with open("countries.txt") as f:
        for line in iter(f.readline, ""):
            print(line, end="")
```

```python
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class LineItem:
    price: int
    quantity: int

    def total_price(self)->int:
        return self.price*self.quantity

def print_totals(items: Iterable[LineItem])->None:
    for item in items:
        print(item.total_price())

def main()->None:
    line_items = [
            LineItem(1, 2),
            LineItem(3, 4),
            LineItem(5, 6),
            ]
    print_totals(line_items)

if __name__ == "__main__":
    main()
```

## Custom Iterators

```python
from dataclasses import dataclass
from typing import Iterable, Self

@dataclass
class InfiniteNumberIterators:
    num: int = 0

    def __iter__(self)->Self:
        return self

    def __next__(self)->int:
        self.num+=1
        return self.num

@dataclass
class NumberIterator:
    max: int
    num: int = 0

    def __iter__(self)->Self:
        return self

    def __next__(self)->int:
        if self.num>=self.max:
            raise StopIteration
        self.num+=1
        return self.num

def main()->None:
    for num in NumberIterator(3):
        print(num)

if __name__ == "__main__":
    main()
```


# Itertools

```python
import itertools

def main()->None:
    # Count from 10
    for i in itertools.count(10):
        print(i)
        if i==15:
            break

    # Repeat
    for i in itertools.repeat(10, 4):
        print(i)

    # Accumulate
    for i in itertools.accumulate(range(1, 11)):
        print(i)

    # Permutations
    items = ["a", "b", "c"]
    perm = itertools.permutations(items) 
    for item in perm:
        print(item)

    # Permutations of two items
    items = ["a", "b", "c"]
    perm = itertools.permutations(items, 2) 
    for item in perm:
        print(item)

    # Combinations of two items
    items = ["a", "b", "c"]
    comb = itertools.combinations(items, 2) 
    for item in comb:
        print(item)

    # Combinations with replacement of two items
    items = ["a", "b", "c"]
    comb = itertools.combinations_with_replacement(items, 2) 
    for item in comb:
        print(item)

    # Change into a list
    comb = list(itertools.combinations_with_replacement(items, 2) )
    print(comb)

    # Chain
    items = ["a", "b", "c"]
    more_items = ["d", "e", "f"]
    chain = list(itertools.chain(items, more_items) )
    print(chain)

    # Filter false elements
    chain = list(itertools.filterfalse(lambda x: x%2==0, range(10)) )
    print(chain)

    # Take while traverses elements until get true
    chain = list(itertools.takewhile(lambda x: x%2==0, range(10)) )
    print(chain)

    # Star map
    star = list(itertools.starmap(lambda x, y: x*y, [(2, 6), (3, 4)]) )
    print(star)

if __name__ == "__main__":
    main()

```
