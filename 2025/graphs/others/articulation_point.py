class Solution:
    
    def articulationPoints(self, V, adj):
        # code here
        time = 1
        visit = set()
        tin = [-1] * V
        low = [-1] * V
        choke = set()
        
        def dfs(node, par):
            nonlocal time
            visit.add(node)
            tin[node] = low[node] = time
            time += 1
            children = 0
            
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit:
                    low[node] = min(low[node], tin[nei])
                else:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    children += 1
                    if low[nei] >= tin[node] and par != -1:
                        choke.add(node)
            if par == -1 and children >= 2:
                choke.add(node)
        
        for i in range(V):
            if i not in visit:
                dfs(i, -1)
        
        return sorted(list(choke)) if len(choke) > 0 else [-1]
    
print(Solution().articulationPoints())

# provide an adjacency matrix to follow the code