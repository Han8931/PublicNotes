
## Keep Your Classes Small

```python
from dataclasses import dataclass

@dataclass
class Body:
    height: int
    blood: str

@dataclass
class Person:
    name: str
    job: str
    age: int
    body: Body

person_body = Body(height=179, blood='O')
person = Person(name="Han", job="student", age=18, body=person_body)
print(person.body.height)
```

## Make Classes Easy to Use

### cached_property
If your property involves computations and it has to be called a lot, then it would be better to set it as `cached_property `
```python
from functools import cached_property

@cached_property
def bmi(self)->float:
	return self.weight/(self.height**2)

@property 
def bmi_category(self)->str:
	if self.bmi<18.5:
		return "Underweight"
	elif self.bmi<25:
```

The `cached_property` computes the value only once. 

>However, note that if the value of `self.weight` has been changed, then `cached_property` does not compute it again. 

Another way to solve the issue it to create a function with `lru_cache` like below

```python
from functools import lru_cache 

@lru_cache
def bmi(weight:float, height:float)->float:
	return weight/(height**2)

@lru_cache 
def bmi_category(bmi_value: float)->str:
	if bmi_value<18.5:
		return "Underweight"
	elif bmi_value <25:
```

`lru_cache` caches the value resulted from the given arguments.

## Use Dependency Injection

