from collections import deque
import heapq
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visit = set()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append([r, c])
                    visit.add((r, c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                    nr, nc = dr + row, dc + col
                    if min(nr, nc) < 0 or max(nr, nc) == n or (nr, nc) in visit:
                        continue
                    visit.add((nr, nc))
                    q.append([nr, nc])
            distance += 1
        
        return (distance-1) if (distance-1) > 0 else -1
    
print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))