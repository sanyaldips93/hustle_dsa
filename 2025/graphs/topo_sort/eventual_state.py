from collections import deque
from typing import List

#bfs
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0] * len(graph)
        adj = {i:[] for i in range(len(graph))}
        for i in range(len(graph)):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return sorted(topo)


#dfs
class Solution2:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        res = []

        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safe[node] = True
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res