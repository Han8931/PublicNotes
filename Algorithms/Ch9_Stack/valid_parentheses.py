"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

This problem is very simple if we know the concept of the stack, but we also have to consider a exceptional case, where stack is empty.
If stack is empty, then it would mean there is no open parentheses.
Also, if all parentheses in the string are valid, then the final stack will be empty.

"""

import pdb

s = "([]{})"

def valid_parentheses(s):

    stack = []
    table = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char not in table:
            stack.append(char)
        # Stack can be empty
        elif not stack or table[char]!=stack.pop():
            return False
    return len(stack)==0

print(valid_parentheses(s))




