"""
You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
"""
import pdb

def search_matrix(matrix, target):
    if not matrix:
        return False

    row, col = 0, len(matrix[0])-1

    while row<=len(matrix)-1 and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            row+=1
        elif matrix[row][col]>target:
            col-=1
    return False

def search_matrix_any(matrix, target):
    return any(target in row for row in matrix)

matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
target = 10
print(search_matrix(matrix, target))
print(search_matrix_any(matrix, target))

#    for i in range(m):
#        for j in range(n):
