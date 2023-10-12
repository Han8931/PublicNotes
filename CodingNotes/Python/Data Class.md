
Let's say we have a class, `Person`. If we print instances of the class, then it wouldn't give me much information about them.
```python

class Person:
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

person1 = Person('Geralt', 'Witcher', 30)
person2 = Person('Yennefer', 'Sorceress', 25)
person3 = Person('Yennefer', 'Sorceress', 25)
```

```python
print(id(person2))
print(id(person3))
print(person1)

print(person2==person3)

140456708401296
140456708404752
<__main__.Person object at 0x7fbea038c8b0>
False
```

By using `dataclass`,  we can simplify the job.
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    job: str
    age: int
```

```sh
140088241927792
140088241923904
Person(name='Geralt', job='Witcher', age=30)
True
```

Sometimes, we wanna compare data as follows:
```python
print(person1>person2)
```

To do this, 
```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int

    def __post_init__(self):
        self.sort_index = self.age
```
- `order=True` allows sorting
- `field` allows set init to be false. Thus, we don't have to initialize it. 
- To suppress printing `sort_index` variable, we can set `repr=False`. This excludes the variable from `__str__` function. 

## Post Init
Sometimes you wanna generate a value from another variable. That's when the `__post_init__` methods come into play.
```python
search_string: str = field(init=False)

def __post_init__(self)->None:
	self.search_string = f"{self.name} {self.address}"
```
The `search_string` is used for searching.

## Default Value
We can also set a default value of variables like 
- `strength:int = 100`
Let's say we wanna set a default value of email addresses of person. It is tempting to set like
- `email_addresses: list[str] = []`
This will cause an issue that all person instances will refer the empty list. To address the issue:
- `email_addresses: list[str] = field(default_factory=list)`
	- Note that we provide a function `list`, instead of instance.
	- It means we can provide any function to the field.
- We can still initialize the value, but we can also prevent this by
	- `field(init=False, default_factory=list)`

## Frozen Dataclass
By freezing the dataclass, we can create read-only objects.
- `@dataclass(frozen=True)`
- Once the class is frozen, we will get an error `self.sort_index = self.age`.
	- To circumvent the issue, we can use `object.__setattr__(self, 'sort_index', self.age)`
- We cannot also set an attribute like `person1.age = 25`

We can set customized `__str__`
```python
    def __str__(self) -> str:
        return f"{self.name} {self.job} {self.age}"
```

### kw_only
- `kw_only=True`, then you have to provide argument names when you set initial values of members

### match_args
- 

### slots
- `slots=True`: it doesn't use `__dict__` anymore, instead it will use slots.
