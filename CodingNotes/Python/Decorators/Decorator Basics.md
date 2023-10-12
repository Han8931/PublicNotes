Decorators are functions (or classes) that provide enhanced functionality to the original function (or class) without the programmer having to modify their structure.

[References](https://realpython.com/primer-on-python-decorators/#decorating-classes "Permanent link")
# Functions

Before you can understand decorators, you must first understand how functions work. For our purposes, **a function returns a value based on the given arguments**. Here is a very simple example:

```python
def add_one(number): 
	return number + 1  
add_one(2) 
3
```

In Python, functions are **first-class objects**.
- This means that **functions can be passed around and used as arguments**, just like any other object (string, int, float, list, and so on). Consider the following three functions:

```python
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
```

Here, `say_hello()` and `be_awesome()` are regular functions that expect a name given as a string. The `greet_bob()` function however, expects a function as its argument. We can, for instance, pass it the `say_hello()` or the `be_awesome()` function to the `greet_bob`:

```python
greet_bob(say_hello)
```

## Inner Functions

It’s possible to define functions _inside other functions_. Such functions are called inner functions. Here’s an example of a function with two inner functions:

```python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

What happens when you call the `parent()` function? Think about this for a minute. The output will be as follows:

Note that the order in which the inner functions are defined does not matter. Like with any other functions, the printing only happens when the inner functions are executed.

Furthermore, the inner functions are not defined until the parent function is called. They are locally scoped to `parent()`: they only exist inside the `parent()` function as local variables. Try calling `first_child()`. You should get an error.

## Returning Functions From Functions

Python also allows you to _use functions as return values_. The following example returns one of the inner functions from the outer `parent()` function:

```python
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
```

- Note that you are returning `first_child` without the parentheses. Recall that this means that you are **returning a reference to the function `first_child`**. 
- In contrast `first_child()` with parentheses refers to the result of evaluating the function. This can be seen in the following example:

```
>>> first = parent(1)
>>> second = parent(2)

>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>

>>> second
<function parent.<locals>.second_child at 0x7f599dad5268>
```

The somewhat cryptic output simply means that the `first` variable refers to the local `first_child()` function inside of `parent()`, while `second` points to `second_child()`.

# Simple Decorators

Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see the magical beast that is the Python decorator. Let’s start with an example:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
```

Can you guess what happens when you call `say_whee()`? Try it:

```
>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```

Put simply: **decorators wrap a function, modifying its behavior.**

Before moving on, let’s have a look at a second example. Because `wrapper()` is a regular Python function, the way a decorator modifies a function can change dynamically. So as not to disturb your neighbors, the following example will only run the decorated code during the day:

```python
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
```

## Syntactic Sugar

The way you decorated `say_whee()` above is a little clunky. First of all, you end up typing the name `say_whee` three times. In addition, the decoration gets a bit hidden away below the definition of the function.

Instead, Python allows you to **use decorators in a simpler way with the `@` symbol**, sometimes called the [“pie” syntax](https://www.python.org/dev/peps/pep-0318/#background). The following example does the exact same thing as the first decorator example:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

So, `@my_decorator` is just an easier way of saying `say_whee = my_decorator(say_whee)`. It’s how you apply a decorator to a function.

## Decorating Functions With Arguments

Say that you have a function that accepts some arguments. 
```python
from decorators import do_twice

@my_decorator 
def greet(name):
    print(f"Hello {name}")

greet("John")
```
Unfortunately, running this code raises an error.

The problem is that the inner function `wrapper()` does not take any arguments, but `name="John"` was passed to it. You could fix this by letting `wrapper()` accept one argument, but then it would not work for the `say_whee()` function you created earlier.

The solution is to use `*args` and `**kwargs` in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments. Rewrite `decorators.py` as follows:

```python

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper
```

## Returning Values From Decorated Functions

What happens to the return value of decorated functions? Well, that’s up to the decorator to decide. Let’s say you decorate a simple function as follows:

```python
@my_decorator 
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
```

```
>>> hi_adam = return_greeting("Adam")
Creating greeting
Creating greeting
>>> print(hi_adam)
None
```
Oops, your decorator ate the return value from the function.

Because the `wrapper()` doesn’t explicitly return a value, the call `return_greeting("Adam")` ended up returning `None`.

To fix this, you need to **make sure the wrapper function returns the return value of the decorated function**. Change your `decorators.py` file:

```python
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
```


# Real World Examples
This is the typical pattern of decorators. 

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```


## Timing Functions

Let’s start by creating a `@timer` decorator. It will measure the time a function takes to execute and print the duration to the console. Here’s the code:
```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
```

## Debugging Code

The following `@debug` decorator will print the arguments a function is called with as well as its return value every time the function is called:

```python
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
```

## Slowing Down Code

This next example might not seem very useful. Why would you want to slow down your Python code? Probably the most common use case is that you want to rate-limit a function that continuously checks whether a resource—like a web page—has changed. The `@slow_down` decorator will sleep one second before it calls the decorated function:

```python
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
```

## Registering Plugins

Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:

```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```

The `@register` decorator simply stores a reference to the decorated function in the global `PLUGINS` dict. Note that you do not have to write an inner function or use `@functools.wraps` in this example because you are returning the original function unmodified.

The `randomly_greet()` function randomly chooses one of the registered functions to use. Note that the `PLUGINS` dictionary already contains references to each function object that is registered as a plugin:

## Is the User Logged In?

The final example before moving on to some fancier decorators is commonly used when working with a web framework. In this example, we are using [Flask](https://realpython.com/tutorials/flask/) to set up a `/secret` web page that should only be visible to users that are logged in or otherwise authenticated:

```python
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
```

# Fancy Decorators

## Decorating Classes

There are two different ways you can use decorators on classes. The first one is very close to what you have already done with functions: you can **decorate the methods of a class**. This was [one of the motivations](https://www.python.org/dev/peps/pep-0318/#motivation) for introducing decorators back in the day.

Some commonly used decorators that are even built-ins in Python are [`@classmethod`, `@staticmethod`](https://realpython.com/instance-class-and-static-methods-demystified/), and [`@property`](https://realpython.com/python-property/). The `@classmethod` and `@staticmethod` decorators are used to define methods inside a class [namespace](https://realpython.com/python-namespaces-scope/) that are not connected to a particular instance of that class. The `@property` decorator is used to customize [getters and setters](https://realpython.com/python-getter-setter/) for [class attributes](https://realpython.com/python-classes/#class-attributes). Expand the box below for an example using these decorators.

## Nesting Decorators

You can **apply several decorators** to a function by stacking them on top of each other:

```python
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
```


## Decorators With Arguments

Sometimes, it’s useful to **pass arguments to your decorators**. For instance, `@do_twice` could be extended to a `@repeat(num_times)` decorator. The number of times to execute the decorated function could then be given as an argument.

This would allow you to do something like this:
```python
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
```

```python
def repeat(num_times):
    def decorator_repeat(func):
		value_list = []
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
				value_list.append(func(*args, **kwargs))
            return value_list 
        return wrapper_repeat
    return decorator_repeat
```

## Classes as Decorators

Recall that the decorator syntax `@my_decorator` is just an easier way of saying `func = my_decorator(func)`. Therefore, if `my_decorator` is a class, it needs to take `func` as an argument in its `.__init__()` method. Furthermore, the class instance needs to be [callable](https://docs.python.org/reference/datamodel.html#emulating-callable-objects) so that it can stand in for the decorated function.

For a class instance to be callable, you implement the special `__call__` method:
```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")
```

The `.__call__()` method is executed each time you try to call an instance of the class:
```
>>> counter = Counter()
>>> counter()
Current count is 1

>>> counter()
Current count is 2

>>> counter.count
2
```

Therefore, a typical implementation of a decorator class needs to implement `.__init__()` and `.__call__()`:
```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")
```

The `.__init__()` method must store a reference to the function and can do any other necessary initialization. The `.__call__()` method will be called instead of the decorated function. It does essentially the same thing as the `wrapper()` function in our earlier examples. Note that you need to use the [`functools.update_wrapper()`](https://docs.python.org/library/functools.html#functools.update_wrapper) function instead of `@functools.wraps`.

