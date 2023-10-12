Unit test is a formal way of testing an unit of program.

# pytest
## Install
- `pip install pytest`
- `pip install pytest-cov`
	- `pytest --cov`: this returns a coverage of test functions 
	- `coverage html`: log test results in html format

`pytest` is a libarary for testing.  
- `pytest test_function.py`

If you wanna create a directory with several testing files, then just put `__init__.py` inside that dir and run 
- `pytest test`, test is the dir name

`python -m unittest [testfile]`

## Example

- `assert`: `assert x == "goodbye", "x should be 'hello'"`

```python
from calc import square
import pytest

def square(n):
    return n*n

# This is a convention test_{func}
def test_negative():
    assert square(-2)==4
    assert square(-3)==9

def test_positive():
    assert square(2)==4
    assert square(3)==9

def test_zero():
    assert square(0)==0

def test_str():
    # Write down what I expect to get 
    # If it successfully raised the error that I expected
    # Then, it will pass the test
    with pytest.raises(TypeError):
        square("cat")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

if __name__=="__main__":
    main()
```
- When we intentially raise an error, then we have to use with `pytest.raises("SomeErrorType")`

```python
def test_pay_order(monkeypatch: MonkeyPatch)->None:
    """
    pay_order function needs inputs. 
    Thus, we need to mock the inputs.
    To this end, we are going to use MonkeyPatch
    """
    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _:inputs.pop(0))
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order)
```

## Sensitive Data
Keep your sensitive data in `.env` file and put it in `.gitignore`

- `pip install python-dotenv`

```python
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") or ""
```
