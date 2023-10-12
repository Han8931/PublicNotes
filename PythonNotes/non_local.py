"""
nonlocal keyword is used in nested functions to reference a variable in the parent function.
The nonlocal keyword can only be used inside nested structures.
"""
def myfunc1():
    x = "John"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1()) 
