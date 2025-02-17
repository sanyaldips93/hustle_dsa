from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i, j, val):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == -1 or (i, j) in visit or grid[i][j] == 0:
                return
            visit.add((i, j))
            grid[i][j] = min(grid[i][j], val)
            dfs(i+1, j, val+1)
            dfs(i-1, j, val+1)
            dfs(i, j+1, val+1)
            dfs(i, j-1, val+1)
            visit.remove((i, j))

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    grid[i][j] = 2147483647
                    dfs(i, j, 0)
        
        return grid
    
print(Solution().islandsAndTreasure([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))