from typing import List
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}
        for time in times:
            src, des, wt = time
            adj[src].append([des, wt])
        
        dist = [float("inf")] * (n+1)
        dist[k] = 0

        q = deque()
        q.append([k, 0])
        
        while q:
            node, cost = q.popleft()
            for nei in adj[node]:
                des, wt = nei
                new_cost = cost + wt
                if new_cost < dist[des]:
                    dist[des] = new_cost
                    q.append([des, new_cost])
        
        res = 0
        for i in range(1, len(dist)):
            if dist[i] == float("inf"):
                return -1
            res = max(res, dist[i])

        return res
    
print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))