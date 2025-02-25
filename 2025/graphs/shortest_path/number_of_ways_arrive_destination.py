from typing import List
from collections import deque
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = {i:[] for i in range(n)}
        for src, des, cost in roads:
            adj[src].append([des, cost])
            adj[des].append([src, cost])
        
        dist = [float("inf")] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap = []
        heapq.heappush(heap, [0,0]) # cost, node

        while heap:
            cost, node = heapq.heappop(heap)
            for des, wt in adj[node]:
                new_cost = cost + wt
                if new_cost < dist[des]:
                    dist[des] = new_cost
                    ways[des] = ways[node]
                    heapq.heappush(heap, [new_cost, des])
                elif new_cost == dist[des]:
                    ways[des] = (ways[des] + ways[node]) % MOD
        
        return ways[n-1]