class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        visit = set()
        stack = []
        
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
            stack.append(node)
        
        for i in range(len(adj)):
            if i not in visit:
                dfs(i)
        
        return stack[::-1]