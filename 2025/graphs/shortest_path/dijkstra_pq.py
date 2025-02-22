import heapq
from typing import Tuple, List

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        pq = []
        heapq.heappush(pq, [src,0])
        dist = [float("inf")] * len(adj)
        dist[src] = 0
        
        while pq:
            node, cost = heapq.heappop(pq)
            for nei in adj[node]:
                des, wt = nei
                if cost + wt < dist[des]:
                    dist[des] = cost + wt
                    heapq.heappush(pq, [des, dist[des]])
            
        return dist