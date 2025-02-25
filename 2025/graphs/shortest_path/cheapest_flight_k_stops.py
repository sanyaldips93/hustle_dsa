import heapq
from typing import List
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for flight in flights:
            source, des, cost = flight
            adj[source].append([des, cost])
        dist = [float("inf")] * n
        dist[src] = 0
        q = deque()
        q.append([src,0,0])

        while q:
            node, cost, steps = q.popleft()
            if steps > k:
                continue
            for nei in adj[node]:
                des, wt = nei
                new_cost = cost + wt
                if new_cost < dist[des]:
                    dist[des] = new_cost
                    q.append([des, new_cost, steps+1])
        
        return dist[dst] if dist[dst] != float("inf") else -1
          
print(Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))