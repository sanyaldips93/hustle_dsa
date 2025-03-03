from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = {i:[] for i in range(n)}
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        time = 1
        tin = [-1] * n
        low = [-1] * n
        bridges = []

        def dfs(node, par):
            nonlocal time
            visit.add(node)
            tin[node] = low[node] = time
            time += 1
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit:
                    low[node] = min(low[node], tin[nei])
                else:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    if low[nei] > tin[node]:
                        bridges.append([node, nei])
        
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
        return bridges
    
print(Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))