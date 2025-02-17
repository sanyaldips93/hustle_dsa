from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque([])
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        def rot(r, c):
            nonlocal fresh
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r+1, c)
                rot(r, c+1)
                rot(r, c-1)
                rot(r-1, c)
            time += 1
        
        return -1 if fresh else time