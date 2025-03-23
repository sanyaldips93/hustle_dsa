from collections import deque
import heapq
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        def bfs(src):
            dist = [float("inf")] * n
            dist[src] = 0
            q = deque()
            q.append(src)

            while q:
                node = q.popleft()
                nextnode = edges[node]
                if nextnode != -1 and dist[nextnode] == float("inf"):
                    dist[nextnode] = dist[node] + 1
                    q.append(nextnode)
            
            return dist
        
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        minimumcost = float("inf")
        res = -1
        for i in range(n):
            if dist1[i] == float("inf") or dist2[i] == float("inf"):
                continue
            if minimumcost > max(dist1[i], dist2[i]):
                minimumcost = max(dist1[i], dist2[i])
                res = i
        
        return res

print(Solution().closestMeetingNode([2,2,3,-1], 0, 1))