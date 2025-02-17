from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or i == rows or j < 0 or j == cols or (i,j) in visit or grid[i][j] == 0:
                return 0
            visit.add((i,j))
            return (1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1))
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    val = dfs(i, j)
                    count = max(count, val) 
        
        return count