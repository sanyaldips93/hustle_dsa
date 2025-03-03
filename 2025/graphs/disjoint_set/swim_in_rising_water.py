import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        heap = []
        heapq.heappush(heap, [grid[0][0], 0, 0]) # cost, r, c
        n = len(grid)

        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return cost
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if min(nr, nc) < 0 or max(nr, nc) == n or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(heap, [max(cost, grid[nr][nc]), nr, nc])