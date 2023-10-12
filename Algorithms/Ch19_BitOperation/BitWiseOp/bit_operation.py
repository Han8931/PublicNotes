
# Boolean Operation
print("="*20)
print("Boolean Operators")
print(f"And: True and False >> {True and False}") 
print(f"Or: True or False >> {True or False}") 
print(f"Not: Not True >> {not True}") 

x = y = True
print(f"Xor: True xor True >> { (x and not y) or (not x and y)}") 

# Bitwise Operation
# You can use bitwise operators to perform Boolean logic on individual bits.
# That’s analogous to using logical operators such as and, or, and not, but on a bit level. 
print("="*20)
print("Bit Operators")
print(f"And: True & False: {True & False}") 
print(f"Or: True | False: {True | False}") 
print(f"Xor: True ^ False: {True ^ False}") 
print(f"Not: ~True: {~True}") 

# Arithmetic Bitwise Operation

print("="*20)
print(f"~12: {~12}") 
print(f"12&13: {12&13}") 
print(f"12|13: {12|13}") 
print(f"25|30: {25|30}") 
print(f"12|1: {12|1}") 
print(f"10<<2: {10<<2}") 

print("="*20)
print(f"bin(0b0110+0b0010): {bin(0b0110+0b0010)}") 
print(f"bin(0b0011*0b0101): {bin(0b0011*0b0101)}") 
print(f"bin(0b1101>>2): {bin(0b1101>>2)}") 

print(f"bin(0b0101^~0b1100): {bin(0b0101^~0b1100)}") 

MASK = 0b1111
print(f"bin(0b0101^(0b1100^MASK)): {bin(0b0101^(0b1100^MASK))}") 

