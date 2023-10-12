---
tags:python
---

## Sorted
### Syntax of sorted() function in Python

```python
sorted(iterable, key, reverse = True)`
```

### Parameters of sorted() function in Python

Three parameters are passed in the sorted() method in Python, which are as follows:

-   **Iterable:** This is the Python object that needs to be sorted. It can either be a sequence, i.e. a list, tuple, or string, or a collection, i.e., a dictionary, set, or a frozenset
-   **Key:** It is an optional parameter. This works as a basis for comparison while sorting.
-   **Reverse:** It is an optional parameter. It is a boolean variable, i.e., if set to True, it sorts the variable in descending order, else it sorts in ascending order. The default value of reverse is false.

### Return Type of sorted() function in Python

The sorted function returns a list of sorted items from whatever iterable you pass in.

### Examples of sorted() function in Python

**Example 1: Using sorted() function with List in Python**

**Code:**

```python
list_variable = [5, 4, 2, 1, 3]
print("Original List: ", list_variable)
print("List returned from Sorted Method: ", sorted(list_variable))
print("List returned from Sorted Method in reverse order: ",
      sorted(list_variable, reverse=True))
```

**Output:**

```plaintext
Original List: [5, 4, 2, 1, 3]
List returned from Sorted Method: [1, 2, 3, 4, 5]
List returned from Sorted Method in reverse order: [5, 4, 3, 2, 1]
```

## Sort()
### Syntax of sort() function in Python

```python
list_name.sort(key, reverse=False)`
```

### Parameters of sort() function in Python

Two parameters are passed in the sort () built-in method, which is as follows:

-   **Key:** It is an optional parameter. This works as a basis for comparison while sorting.
-   **Reverse:** It is an optional parameter. It is a boolean variable, i.e., if set to True, it sorts the variable in descending order, else it sorts in ascending order. The default value of reverse is false.

### Return Type of sort() function in Python

Sort() function makes changes to the original sequence. Therefore, its return type is None.