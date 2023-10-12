
# Dynamic v.s. Static Typing

Python is a _dynamically_ typed language. What does that mean?

- Type declarations are not required. I can define the following function without ever specifying what types I expect the arguments to be, nor do I have to name a return type:

```python
def my_function(a, b, c):
    return a + b - c  
```

- Types are handled and checked at runtime. I can run `my_function` with either integers, floats or a mix of both as input. The return type depends on the input:

```python
result = my_function(5, 3, 2)
# type(result) -> int

result = my_function(5.1, 3, 2)
# type(result) -> float
```

Comparing this to C, which is a _statically typed language_, we see we have to provide type declarations:

```c
int my_function(int a, int b, int c) { return a + b - c; }
```

Providing any other type would be illegal. The following would not compile:

```c
int result = my_function(5.1, 3, 2); 
```

That is a benefit of statically typed language: types are checked at compile time, so you can not run into any issues with types at runtime. In Python you may encounter issues _at runtime_ that you would never have with a statically typed language.  

On the other hand, dynamically typed languages are more flexible when it comes to types that are accepted. And they do not require type declarations, which is great for lazy programmers.

# Duck Typing

Dynamic typing is also called _duck typing_, because

> _If it walks like a duck and it quacks like a duck, then it must be a duck._

Or in other words: if any object has the required functionality, then we should accept it as an argument.

For example, suppose that we have a class named `Duck`, and this class can walk and quack:

```python
class Duck:
    def walk(self):
        ...

    def quack(self):
        ...   
```

Then we can make an instance of this class and make it walk and quack:

```python
duck = Duck()
duck.walk()
duck.quack() 
```

Now if we have a class `Donkey` that can walk, but it can not quack:

```python
class Donkey:
    def walk(self):
        ...
```

Then if we try to make an instance of the donkey walk and quack:

```python
duck = Donkey()
duck.walk()
duck.quack() 
```

We will get an `>> AttributeError: 'Donkey' object has no attribute 'quack’`. Note that we only get this _at runtime!_

However, we can replace `duck` with any other class that can walk and can quack. For example:

```python
class ImpostorDuck:
    def walk(self):
        ...

    def quack(self):
        not_quite_quacking()

duck = ImpostorDuck()
duck.walk()
duck.quack() 
```

So, wrapping up: Python is a dynamically typed language, which is great because it gives lots of flexibility and type declarations are not required. But no type checking happens except at runtime, which can lead to unexpected issues. Which leads us to **type hints**!

# Type Hints

Type Hints, or _optional static typing_, were introduced in Python 3.5 to overcome this downside. It lets you _optionally_ specify types of arguments and return values, which can then be checked by a static type checker such as [mypy](http://mypy-lang.org).

For example, suppose we have a type `Duck` that can swim and eat bread:

```python
class Duck:
    def eat_bread(self):
        ...  

    def swim(self):
        ... 
```

We can then define a function `feed_bread` that makes a Duck eat bread. We can specify the type of the argument to be of type `Duck`:

```python
def feed_the_duck(duck: Duck):
    duck.eat_bread()

duck = Duck() 
feed_the_duck(duck)
```

Now trying to feed bread to a Monkey, for example, will not work:

```python
class Monkey:
    def eat_bananas(self):
        ...

    def climb_tree(self):
        ...

monkey = Monkey() 
feed_the_duck(monkey)
```

At runtime, this will give you: `>> AttributeError: 'Monkey' object has no attribute 'eat_bread’`.

But mypy can spot issues like these before you run your code. In this case, it will tell you:

```
error: Argument 1 to "feed_the_duck"  has incompatible type "Monkey"; expected "Duck"
```

These type hints can make your life as developer much easier, but they aren’t perfect. For example, if we want to make `feed_bread` more generic such that it can also accept other types of animal, we need to explicitly list all accepted types:

```python
from typing import Union

class Pig:
    def eat_bread(self):
        pass

def feed_bread(animal: Union[Duck, Pig]):
    animal.eat_bread()
```

And another downside: if you use code as above that is provided by an external package that is not under your control (let’s suppose it is called `animals`), you can not use it for your own types. For example, my baby son Mees’ favourite activities include eating bread and drinking milk:

```python
from animals import feed_bread

class Mees:
    def eat_bread(self):
        pass

    def drink_milk(self):
        pass 

mees = Mees() 
feed_bread(mees)
```

At runtime the above code will work perfectly fine, but mypy will complain:

```
>> error: Argument 1 to "feed_bread" has incompatible type "Mees";  expected "Union[Duck, Pig]"
```

If we do not have control over the `animals` package, there is nothing be can do about this – except tell mypy to ignore the offending line.

So, wrapping up: type hints are great because they give you the option to have static type checking. Still there are no obligations to add type declarations, but if you do, you get some of the benefits of a statically typed language. But the inability to adapt type hints of imported code gives conflicts between the dynamic typing nature of Python and the static type hints.

# ABCs

[Abstract Base Classes](https://docs.python.org/3/library/abc.html) take away some of the pain of the conflict described above. As the name says, they are _base classes_-classes that you are supposed to inherit from- but they can not be instantiated. They are used to define the interface of what the sub-classes of the ABC should look like.

For example (and forgive me for assuming that all animals can walk):

```python
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass  # Needs implementation by subclass
```

Instantiating this class is impossible: `my_animal = Animal()` will yield `>> TypeError: Can't instantiate abstract class Animal with abstract methods walk`.

However, if we define a subclass, we can instantiate it:

```python
class Duck(Animal):
    def walk(self):
        ...  

duck = Duck()
assert isinstance(duck, Animal)  # <-- True
```

For a more practical example, one may create an ABC called `EatsBread` that defines that its subclasses can indeed eat bread (or, in other words, they must have a method with the signature `eat_bread(self)`):

```python
from abc import ABCMeta, abstractmethod

class EatsBread(metaclass=ABCMeta):
    @abstractmethod
    def eat_bread(self):
        pass

class Duck(EatsBread):
    def eat_bread(self):
        ...

class Pig(EatsBread):
    def eat_bread(self):
        ...

def feed_bread(animal: EatsBread):
    animal.eat_bread()
```

Now if I were to use this implementation of `feed_bread` in my code of `Mees` – I can make `Mees` a subclass of `EatsBread` and all will be fine:

```python
from animals import EatsBread, feed_bread

class Mees(EatsBread):
    def eat_bread(self):
        ...

    def drink_milk(self):
        ...

feed_bread(Mees())  # <-- OK at runtime and for mypy
```

Although this is much better – this still is not perfect. Often base classes are not easily exposed, meaning I have to have ugly imports to get what I need:

```python
from animals import feed_bread
from animals.base.eats import EatsBread
```

In addition you have to either inherit from the base class (or explicitly register your class as a subclass, e.g. `EatsBread.register(Mees)`) for this to work – which is not as nice as the implicit behaviour of duck typing.

And still there can be situations which would not _quite_ work. Suppose we use two external packages:

From package `animals`:

```python
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass  

class Dog(Animal):
    def walk(self):
        ...

def walk_animal(animal: Animal):
    animal.walk()
```

And from package `llamas`:

```python
class Llama:
    def walk(self):
        ...
```

Now if you combine those in your code:

```python
from animals import walk_animal
from llamas import Llama

llama = Llama()
walk_animal(llama)  # <-- Not OK for mypy
```

This last line will work fine at runtime – but as `Llama` does not inherit from `Animal`, mypy will complain.

One can solve this by making `Llama` a virtual subclass of `Animal`:

```python
Animal.register(Llama)  

llama = Llama()
walk_animal(llama)  # <-- OK
```

But I would say that this is far from pretty.

Wrapping up once more: ABCs provide structure to your types, which is great. This means that type hints do not need updates for new subclasses. But we may still have issues combining classes from multiple packages. And all this typing -be it inheriting or as virtual subclasses- need to happen explicitly, which conflicts with the dynamic and implicit nature of dynamic typing.

# Protocols

And this is where protocols come in. A protocol is a special case of ABC which works implicitly:

```python
from typing import Protocol

class EatsBread(Protocol):
    def eat_bread(self):
        pass

def feed_bread(animal: EatsBread):
    animal.eat_bread()

class Duck:
    def eat_bread(self):
        ...

feed_bread(Duck())  # <-- OK
```

In the above code, `Duck` is implicitly considered to be a subtype of `EatsBread`. There is no need to explicitly inherit from the protocol. Any class that implements all attributes and methods defined in the protocol (with matching signatures) is seen as a subtype of that protocol.

So if we were to use the `feed_bread` function from package `animals`:

```python
from animals import feed_bread

class Mees:
    def eat_bread(self):
        ...

    def drink_milk(self):
        ...

feed_bread(Mees())  # <-- OK
```

Here `Mees` is also implicitly a subtype of `EatsBread`. Again there is no need to explicitly specify that: as long as the signatures match it just works! This is why protocols are also called _static duck typing_.

Note that all this only works _while type checking_: not at runtime! If you do want this to work at runtime, you can use the [`runtime_checkable`-decorator](https://docs.python.org/3/library/typing.html#typing.runtime_checkable).

Wrapping up one last time: protocols are awesome, because:

- There is no need to explicitly inherit from a protocol or register your class as a virtual subclass.
- There are no more difficulties combining packages: it works as long as the signatures match.
- We now have the best of both worlds: static type checking of dynamic types.

