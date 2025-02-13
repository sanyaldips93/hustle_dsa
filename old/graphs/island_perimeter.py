from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            visit.add((i, j))
            perim = dfs(i + 1, j)
            perim += dfs(i - 1, j)
            perim += dfs(i, j + 1)
            perim += dfs(i, j - 1)
        
            return perim
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
        
print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))