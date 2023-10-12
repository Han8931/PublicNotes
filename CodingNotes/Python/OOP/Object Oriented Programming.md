# OOP 

```python
import csv

class Item:
    # Class Attribute
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self, name, price, quantity):
        assert price >= 0, f"Price {price} is not greater than zero!" 
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"  

        self.name = name
        self.price = price
        self.quantity = quantity

		# Whenever a class creates an instance, 
		# it will append the instance to the list `all`
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discout(self):
        self.price = self.price*Item.pay_rate
        # self.price = self.price*Item.pay_rate

	# Simply, classmethod is a method accessble from class
    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
			# whenever an instance is created, it will be appended at 'all' list
            Item(
                    name=item['name'],
                    price=int(item['price']),
                    quantity=int(item['quantity'])
            )

	# staticmethod is a like a regular function
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # Count out the floats that are
            return num.is_integer() # This is just a built-in fnc
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(7))
# print(Item.instantiate_from_csv())
# print(Item.all)
```

## Static method

The reason to use `staticmethod` is if you have something that could be written as a standalone function (not part of any class), but you want to keep it within the class because it's somehow semantically related to the class. (For instance, it could be a function that doesn't require any information from the class, but whose behavior is specific to the class, so that subclasses might want to override it.) In many cases, it could make just as much sense to write something as a standalone function instead of a staticmethod.

A static methods creates a method which does not receive an implicit first argument at all; accordingly it won't be passed any information about the instance on which it was called.
## Class method
A class method receives the class as the implicit first argument, just like an instance method receives the instance.

# Inheritance

```python
class Phone(Item):
    all = []

    def __init__(self, name, price, quantity, broken_phone):
        # Call to super function to have access to all attributes and methods
        super().__init__(
                name, price, quantity
                )
        assert broken_phone >= 0, f"Broken Phone {broken_phone} is not greater than zero!"  

        self.broken_phone = broken_phone

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phone})"
```


# Property Decorator: Read only property

```python
@property
def price(self):
	return self.__price
```
- The `price`  becomes a read only value. 

We can also set a rule for changing a value of a variable.

```python 
# Property decorator: Read only property
@property
def name(self):
	return self.__name

# It enables to set a value to name
@name.setter
def name(self, value):
	if len(value)>10:
		raise Exception("The name is too long!")
	self.__name = value 
```
