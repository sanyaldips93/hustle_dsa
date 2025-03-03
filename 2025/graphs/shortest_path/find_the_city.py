from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
        
        for u,v,wt in edges:
            dist[u][v] = wt
            dist[v][u] = wt


        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))
        

        rescity = -1
        mincount = n
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if (count < mincount) or (count == mincount and i > rescity):
                mincount = count
                rescity = i

        return rescity
    

class Solution2:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # create adjacency list
        adj = {i:[] for i in range(n)}
        for u,v,wt in edges:
            adj[u].append([v, wt])
            adj[v].append([u, wt])
        
        def dijkstra(adj, src):
            dist = [float("inf")] * n
            dist[src] = 0
            heap = []
            heapq.heappush(heap, [0, src])

            while heap:
                cost, node = heapq.heappop(heap)
                for nei, wt in adj[node]:
                    if dist[nei] > cost + wt:
                        dist[nei] = cost + wt
                        heapq.heappush(heap, [cost+wt, nei])
            
            return dist

        
        minReach = float("inf")
        rescity = -1
        for i in range(n):
            dist = dijkstra(adj, i)
            print(dist)
            reachable = sum(1 for n in dist if n <= distanceThreshold)

            if reachable <= minReach:
                minReach = reachable
                rescity = i
            
        return rescity