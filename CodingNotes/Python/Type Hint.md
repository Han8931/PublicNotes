Reference: 
- [Link](https://sjquant.tistory.com/69)
- ArajanCode
### Callable Types

Callable type hint can define types for callable functions.
```python
from typing import Callable
Callable[[Parameter types, ...], return_types] 
```
- Callable objects are functions, classes, and so on. 
- Type `[input types]` and return types

```python
def on_some_event_happened(callback: Callable[[int, str, str], int]) -> None:
    ...

def do_this(a: int, b: str, c:str) -> int:
    ...

on_some_event_happened(do_this)
```

### Ellipsis  ...
- It means the collection is of arbitrary length, but all the elements will be the same type, as defined by the first type specified. 

### Union 
For multiple types

```python
def process_message(msg: Union[str, bytes, None]) -> str:
```

### Optional 
```python
def eat_food(food: Optional[str]) -> None:
```
`food` can be either `str` or `None`.

### TypeVar
This is a special type for generic types. 

```python
from typing import Sequence, TypeVar, Iterable

T = TypeVar("T")  # `T` is typically used to represent a generic type variable

def batch_iter(data: Sequence[T], size: int) -> Iterable[Sequence[T]]:
    for i in range(0, len(data), size):
        yield data[i:i + size]
```

Since the generic type is used, `batch_iter` function can take any type of `Sequence` type `data`. For instance, `Sequence[int]`, `Sequence[str]`, `Sequence[Person]`

If we use `bound`, then we can restrict the generic type. For example, 
```python
from typing import Sequence, TypeVar, Iterable, Union

T = TypeVar("T", bound=Union[int, str, bytes])

def batch_iter(data: Sequence[T], size: int) -> Iterable[Sequence[T]]:
    for i in range(0, len(data), size):
        yield data[i:i + size]
```

Thus, the following code will show an error as it takes a list of float numbers:
```python
batch_iter([1.1, 1.3, 2.5, 4.2, 5.5], 2)
```

### ETC
```python
from typing import List, Tuple, Dict

names: List[str]
location: Tuple[int, int, int]
coount_map: Dict[str, int]
```

