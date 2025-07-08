from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                wt = abs(x1-x2) + abs(y1-y2)
                adj[i].append([j, wt])
                adj[j].append([i, wt])
        
        visit = set()
        q = []
        heapq.heappush(q, [0, 0])
        sum = 0

        while q:
            cost, node = heapq.heappop(q)
            if node in visit: continue
            visit.add(node)
            sum += cost
            for nei, wt in adj[node]:
                if nei not in visit:
                    heapq.heappush(q, [wt, nei])
        
        return sum