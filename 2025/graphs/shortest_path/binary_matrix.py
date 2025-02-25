from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = cols = len(grid)
        visit = set()
        q = deque()
        q.append([0,0,1])
        dir = [[1,0], [0,1], [-1,0], [0,-1], [-1,-1], [1,1], [-1,1], [1,-1]]

        while q:
            r, c, length = q.popleft()
            if (r, c) == (rows-1, cols-1):
                return length
            for dr, dc in dir:
                nr = dr + r
                nc = dc + c
                if (nr, nc) not in visit:
                    visit.add((nr, nc))
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc]:
                      continue
                    q.append([nr, nc, length+1])
        return -1

print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))