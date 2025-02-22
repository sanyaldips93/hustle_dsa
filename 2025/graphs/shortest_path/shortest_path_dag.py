from typing import List
from collections import deque


class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        # create adjaceny list
        adj = {i:[] for i in range(V)}
        for edge in edges:
            src = edge[0]
            des = edge[1]
            wt = edge[2]
            adj[src].append([des, wt])
        
        # topo sort using dfs
        stack = []
        visit = set()
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                n, w = nei
                if n not in visit:
                    dfs(n)
            stack.append(node)
        
        
        for i in range(len(adj)):
            if i not in visit:
                dfs(i)
       
        
        # calculate distance
        dist = [float("inf")] * V
        dist[0] = 0
       
        while stack:
            node = stack.pop()
            if dist[node] != float("inf"):
                for nei in adj[node]:
                    des = nei[0]
                    wt = nei[1]
                    dist[des] = min(dist[des], dist[node]+wt)
                
        
        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist