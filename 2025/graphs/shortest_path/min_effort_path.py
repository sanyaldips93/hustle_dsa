import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        q = []
        heapq.heappush(q, [0,0,0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0

        while q:
            steps, r, c = heapq.heappop(q)
            if r == rows - 1 and c == cols - 1:
                return steps
            dir = [[1,0], [0,1], [-1,0], [0,-1]]
            for dr, dc in dir:
                nr = dr + r
                nc = dc + c
                if min(nr, nc) < 0 or nr == rows or nc == cols:
                    continue
                effort = max(steps, abs(heights[nr][nc] - heights[r][c]))
                if effort < dist[nr][nc]:
                    dist[nr][nc] = effort
                    heapq.heappush(q, [effort, nr, nc])
        
        return 0