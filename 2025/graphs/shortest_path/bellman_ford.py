class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist = [100000000] * V
        dist[src] = 0
        for i in range(V-1):
            for u,v,wt in edges:
                if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        
        for u,v,wt in edges:
            if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                return [-1]
        
        return dist
    
print(Solution().bellmanFord(3, [[0,1,5], [1,0,3], [1,2,-1], [2,0,1]], 0))

# 0, inf, inf
# 0, 5, 4
# 0, 5, 3
# 0, 5, 2