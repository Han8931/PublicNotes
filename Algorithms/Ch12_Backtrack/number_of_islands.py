"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

import pdb

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def numIslands(grid):
    m,n = len(grid), len(grid[0])

    def dfs(i, j):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
            return 

        grid[i][j]=0

        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i-1, j)
        dfs(i, j-1)
    
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1':
                dfs(i,j)
                count+=1

    return count

print(numIslands(grid))
                

