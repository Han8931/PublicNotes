Given,  A-> B-> C-> D-> E-> F-> G
Swap,  B-> A-> D-> C-> F-> E-> G

```python
def swapNodesPairs(head:Node)->Node:
    if not head or not head.next:
        return head

    temp = head.next
    head.next = swapNodesPairs(temp.next)
    temp.next = head
    return temp
```

### 1) Split the problem into a recursion form
















