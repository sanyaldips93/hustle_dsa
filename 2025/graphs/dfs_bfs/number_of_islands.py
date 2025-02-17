from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or i == rows or j < 0 or j == cols or (i, j) in visit or grid[i][j] == '0':
                return
            visit.add((i,j))
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    count += 1
                    dfs(i, j)
        
        return count
