
# Function
## 1. Do One Thing, and Do It Well
## 2. Separate Commands from Queries

_CQS_ (Command-Query Separation) is a design principle that states that a method (or function) is either a _COMMAND_ that performs an action OR a _QUERY_ that returns data to the caller, but never both.
- In simpler terms, "asking a question shouldn't change the answer".
- More simply, don't keep the result of commands. Always separate it!
```python
def function():
	output = compute
	return output
```

Do this
```python
def function():
	return compute
```

## 3. Only Request Information You Actually Need
For instance, when you pass arguments to a function, don't pass unrelated information. 
```python
def validate_card(customer: Customer)
```

You don't need a whole information about customer to validate the customer's card.
```python
def validate_card(card_number: str, name:str, epx_year: int)
```

## 4. Keep the Number of Parameters Minimal
- Parameter: a part of function definition
- Argument: values

```python
@dataclass
class Customer:
	name: str
	phone: int
	card_number: str
	exp_year: int
```

Split like this.

```python
@dataclass
class Card:
	card_number: str
	exp_year: int

@dataclass
class Customer:
	name: str
	phone: int
	card: Card
```

## 5. Don't Create and Use an Object in the Same Place. 

When you pass an object to a function, don't instantiate an object inside a function. 

## 6. Don't Use (Boolean) Flag Parameters
## 7. Remember That Functions Are Objects



