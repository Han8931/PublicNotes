# Introduction
To precisely represent monetary values, we can consider...
- Float numbers are fast but they are often problematic since they are not accurate.

## Decimal
- Decimal could be an option, but it tends to be slow. More critically, decimal is a specific for Python. If you want to store them in another format, then you need to convert them. 
```python
from decimal import Decimal, getcontext 

def decimal_main():
    print(1.1+2.2)
    # getcontext().prec = 2 # This controls the precision
    print(Decimal(1.1)+Decimal(2.2))
    print(Decimal('1.1')+Decimal('2.2'))
```

You should have used sting argument in constructor Decimal('1.1') instead of Decimal(1.1). You have lost all you precision when created float 1.1, because float 1.1 is not exactly equal to 1.1 And that is because floats are represented in binary values, but value 1.1 in binary system is periodic, so it cannot be written precisely.

## Integer
The Integer type is relatively fast and memory efficient. So we can use it like

```python
def to_dollars(amount:int)->str:
    return f"${amount/100:.2f}"

def main()->None:
    int_balance = 10_000
    int_withdrawl = 4237
    int_deposit = 10

    int_result = int_balance-int_withdrawl+int_deposit
    print(f"Using integers: {to_dollars(int_result)}") 

if __name__ =="__main__":
    main()
```

```python

@dataclass
class Money:
    amount_cents: int = 0
    currency_symbol: str = "$"

    @classmethod
    def mint(cls, amount: Decimal | float, currency_symbol: str = "$") -> Self:
        return cls(int(amount * 100), currency_symbol)

    def __str__(self):
        amount = self.amount_cents / 100
        return f"{self.currency_symbol}{amount:.2f}"

    def __add__(self, other: Self) -> Self:
        if isinstance(other, Money):
            return Money(self.amount_cents + other.amount_cents, self.currency_symbol)

    def __sub__(self, other: Self) -> Self:
        if isinstance(other, Money):
            return Money(self.amount_cents - other.amount_cents, self.currency_symbol)
```

## Numpy

