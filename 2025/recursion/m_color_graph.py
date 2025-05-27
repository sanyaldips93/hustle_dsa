class Solution:
    def graphColoring(self, v, edges, m):
        color = [0] * v
        adj = {i:[] for i in range(v)}
        for u1,v1 in edges:
            adj[u1].append(v1)
            adj[v1].append(u1)
        
        def isSafe(node, clr):
            for k in range(v):
                if k in adj[node] and color[k] == clr:
                    return False
            return True
        
        def backtrack(node):
            if node == v: return True
            
            for k in range(1, m+1):
                if isSafe(node, k):
                    color[node] = k
                    if backtrack(node+1): return True
                    color[node] = 0
            return False
        
        return backtrack(0)

print(Solution().graphColoring(3,  [[0, 1], [1, 2], [0, 2]], 2))