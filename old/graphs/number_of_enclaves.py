from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visit = set()
        land = 0
        border = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r == R or c == C or 
                not grid[r][c] or (r, c) in visit):
                return 0
            visit.add((r, c))
            res = 1
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dir:
                res += dfs(r + dr, c + dc)
            return res
        
        for r in range(R):
            for c in range(C):
                land += grid[r][c]
                if grid[r][c] and (r, c) not in visit and (c in [0, C - 1] or r in [0, R - 1]):
                    border += dfs(r, c)
        
        return land - border
