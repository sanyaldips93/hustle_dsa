from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        rows = len(grid)
        cols = len(grid[0])
        pac, alt = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if r < 0  or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, grid[r][c])
            dfs(r-1, c, visit, grid[r][c])
            dfs(r, c+1, visit, grid[r][c])
            dfs(r, c-1, visit, grid[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, grid[0][c])
            dfs(rows-1, c, alt, grid[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, grid[r][0])
            dfs(r, cols-1, alt, grid[r][cols-1])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])
        
        return res