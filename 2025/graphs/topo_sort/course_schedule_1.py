from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i:[] for i in range(numCourses) }
        for dest, src in prerequisites:
            adj[src].append(dest)
        
        indegree = [0] * numCourses
        for i in range(len(adj)):
            for node in adj[i]:
                indegree[node] += 1
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
        
        return len(topo) == numCourses