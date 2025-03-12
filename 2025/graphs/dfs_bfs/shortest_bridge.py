from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        q = deque()

        def dfs(r, c):
            if min(r, c) < 0 or max(r, c) == n or grid[r][c] == 0 or (r, c) in visit:
                return
            visit.add((r, c))
            q.append([r, c, 0])
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        def bfs():
            while q:
                r, c, steps = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if min(nr, nc) < 0 or max(nr, nc) == n:
                        continue
                    if (nr, nc) in visit:
                        continue
                    if grid[nr][nc]:
                        return steps
                    visit.add((nr, nc))
                    q.append([nr, nc, steps+1])
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()
