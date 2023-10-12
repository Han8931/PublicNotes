---
tags:python
---

[Reference](https://realpython.com/python-variables/)

# Object References

What is actually happening when you make a variable assignment? This is an important question in Python, because the answer differs somewhat from what you’d find in many other programming languages.

Python is a highly object-oriented language. In fact, virtually every item of data in a Python program is an object of a specific type or class. (This point will be reiterated many times over the course of these tutorials.)

Consider this code:

```python
print(300)
```
When presented with the statement print(300), the interpreter does the following:
- Creates an integer object
- Gives it the value 300
- Displays it to the console

A Python variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name. But the data itself is still contained within the object.

Now consider the following statement:

`>>> m = n`

What happens when it is executed? 
- **Python does not create another object. **
- It simply **creates a new symbolic name or reference**, `m`, which points to the same object that `n` points to.

<img src="https://files.realpython.com/media/t.d368386b8423.png" width=50%>


Next, suppose you do this:
`>>> m = 400`
Now Python creates a new integer object with the value `400`, and **`m` becomes a reference to it.**

<img src="https://files.realpython.com/media/t.d476d91592cd.png" width=60%>

Lastly, suppose this statement is executed next:

`>>> n = "foo"`

Now Python creates a string object with the value `"foo"` and makes `n` reference that.

<img src="https://files.realpython.com/media/t.344ab0b3aa8c.png" width=60%>


There is no longer any reference to the integer object `300`. It is orphaned, and there is no way to access it.

When the number of references to an object drops to zero, it is no longer accessible. At that point, its lifetime is over. Python will eventually notice that it is inaccessible and reclaim the allocated memory so it can be used for something else. In computer lingo, this process is referred to as [garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29).

