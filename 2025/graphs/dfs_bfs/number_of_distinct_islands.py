import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        unique = set()
        
        def dfs(r, c, rr, rc, shape):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 0:
                return
            visit.add((r, c))
            shape.append((r-rr, c-rc))
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(r+dr, c+dc, rr, rc, shape)
        
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    shape = []
                    dfs(r, c, r, c, shape)
                    unique.add(tuple(shape))
        
        return len(unique)
