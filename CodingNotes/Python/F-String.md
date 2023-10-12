# Basics

```python
import datetime
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str

def main():
    number = 800
    print(f"The number is: {number}.")  
    print(f"The number is: {number:x}.")  # Hexadecimal 
    print(f"The number is: {number:o}.")  # Octa
    print(f"The number is: {number:e}.")  # Exponential
    print(f"{100.234235123:.3f}.") 
    print(f"{44000000000:,.2f}.") # Comma separator with a precision level
    print(f"{44000000000:_.2f}.") # underscore separator with a precision level
    print(f"{0.234235:%}.") # Percentage
    print(f"{0.234235:.1%}.") # Percentage

    # Alignment
    for number in range(5, 15):
        print(f"The number is: {number:4}.")  # With some empty space


if __name__ == "__main__":
    main()
```

```python
def main():
    greet = "Hi"
    print(f"{greet}") 
    print(f"{greet:>4}") # Put 4 spaces to the left
    print(f"{greet:^4}") # Align to the center
    print(f"{greet:_^4}") # Put underscores
    print(f"{greet:_>4}") # Put underscores
    print(f"{greet:_<4}") # Put underscores

```

# Data Classes, str and repr

- `__str__`: user friendly
- `__repr__`: deverloper friendly

```python
@dataclass
class User:
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

def main():
    user = User("Elon", "Musk")
    print(f"User: {user}") 
    print(f"User: {user!r}") # call repr method
    print(f"User: {repr(user)}") # Equivalent to the above method

    name = "Elon"
    print(f"Who wants to buy Twitter? {name}") 
    print(f"Who wants to buy Twitter? {name!r}")  # Put quotes around the text
```

# Formatting Dates and Times

```python
import datetime 

today = datetime.datetime.now()
print(f"Simple date printing: {today}") 
print(f"{today:%H:%M:%S.%f}") # .%f : milliseconds
print(f"{today:%Y:%m:%d}")
print(f"{today:%y:%m:%d}") # y displays only last two digits of the year
print(f"{today:%D}") 
print(f"{today:%T}") # Time
print(f"Today is a {today:%A}") # Day, Monday, Sunday...
print(f"Today is a {today:%A %B %d %y}") # B: Month
```

# Printing Variables for Debugging Purposes

```python
    x = 45
    y = 78
    print(f"{x=} {y=}")  # This print x=45 y=78
    print(f"{x = } {y = }")  # This print x = 45 y = 78 with white spaces
```

# Multi-Line Strings

```python
    name = "Arajan"
    country = "The Netherlands"
    channel = "Arajan Codes"
    sentence = (
            f"Hi, I'm {name}",
            f"I'm from {country}",
            f"I run a YT channel called {channel}"
            )

    print(f"{sentence}")  # Print as a tuple

    sentence = (
            f"Hi, I'm {name}"
            f"I'm from {country}"
            f"I run a YT channel called {channel}"
            )

    print(f"{sentence}")  # Print as a single sentence
```

# F-String Performance 

In short, F-string is the fastest.

```python
import timeit
from string import Template

TEMPLATE = Template("$name is from $country")

def template():
    name = "Arajan"
    country = "The Netherlands"
    _ = TEMPLATE.substitute(name=name, country=country)

def perc_format():
    name = "Arajan"
    country = "The Netherlands"
    _ = "%s is from %s" % (name, country)

def f_string():
    name = "Arajan"
    country = "The Netherlands"
    _ = f"{name} is from {country}"

def main():
    print(
            "perc_format:",
            timeit.timeit(
                perc_format,
                number=10000,
                ),
            )
    print(
            "f_string:",
            timeit.timeit(
                f_string,
                number=10000,
                ),
            )

    print(
            "template:",
            timeit.timeit(
                template,
                number=10000,
                ),
            )
```






