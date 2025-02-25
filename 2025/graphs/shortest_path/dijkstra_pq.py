import heapq
from typing import Tuple, List

class Solution:
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        
        q = ([[src,0]])
        dist = [float("inf")] * len(adj)
        dist[src] = 0
        
        while q:
            src, wt = heapq.heappop(q)
            # if the distance to the node in question is infinity, there is no point traversing it.
            # the chances of not hitting this line is negative.
            if dist[src] != float("inf"):
                for des, cost in adj[src]:
                    if cost + wt < dist[des]:
                        dist[des] = cost + wt
                        heapq.heappush(q, [des, dist[des]])
        
        for i in range(len(dist)):
            # if there are unreachabe nodes, mark their distance -1
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist