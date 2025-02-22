from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        q = deque()
        indegree = [0] * len(adj)
        for i in range(len(adj)):
            for node in adj[i]:
                indegree[node] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                
        topo = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                topo.append(node)
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        
        return topo