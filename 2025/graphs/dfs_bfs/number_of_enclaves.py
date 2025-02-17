from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        lands = 0
        grids = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            res = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return res

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    lands += 1
                if grid[r][c] and (r, c) not in visit and (c in [0, cols-1] or r in [0, rows-1]):
                    grids += dfs(r, c)

        return lands - grids