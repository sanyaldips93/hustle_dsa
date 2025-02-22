from collections import deque


class Solution:
    def shortestPath(self, adj, src):
        q = deque()
        q.append([src, 0])
        dist = [float("inf")] * len(adj)
        visit = set()
        
        while q:
            node, cost = q.popleft()
            visit.add(node)
            if cost < dist[node]:
                dist[node] = cost
            for nei in adj[node]:
                if nei not in visit:
                    q.append([nei, cost+1])
        
        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist


print(Solution().shortestPath([[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], 0))