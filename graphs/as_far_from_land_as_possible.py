from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        N = len(grid)
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append([r, c])
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        res = -1
        while q:
            r, c = q.popleft()
            res = grid[r][c]
            for dr, dc in dir:
                newr, newc = r+dr, c+dc
                if min(newr, newc) >= 0 and max(newr, newc) < N and grid[newr][newc] == 0:
                    q.append([newr, newc])
                    grid[newr][newc] = 1 + grid[r][c]
        return res - 1 if res > 1 else -1

print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))