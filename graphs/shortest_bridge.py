from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        L = len(grid)
        visit = set()
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        def isinvalid(r, c):
            return r < 0 or c < 0 or c == L or r == L
        def dfs(r, c):
            if isinvalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in dir:
                dfs(r + dr, c + dc)
        def bfs():
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    [r, c] = q.popleft()
                    for dr, dc in dir:
                        cr = r + dr
                        cc = c + dc
                        if isinvalid(cr, cc) or (cr, cc) in visit:
                            continue
                        if grid[cr][cc]:
                            return res
                        q.append([cr, cc])
                        visit.add((cr, cc))
                res += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()


        