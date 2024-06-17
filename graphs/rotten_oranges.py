from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh, time = 0, 0

        def rot(r, c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: fresh += 1
                elif grid[i][j] == 2: q.append([i, j])

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)
            time += 1
        
        return -1 if fresh else time

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))