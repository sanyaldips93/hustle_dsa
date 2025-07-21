# Problem - https://leetcode.com/problems/minimum-height-trees/description
# Pattern - Finding the centroid of a graph.

from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        
        adj = defaultdict(list)
        edges_per_node = defaultdict(int)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            edges_per_node[u] += 1
            edges_per_node[v] += 1
        
        q = deque()
        for node, edges in edges_per_node.items():
            if edges == 1:
                q.append(node)
        
        while q and n > 2:
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in adj[node]:
                    edges_per_node[nei] -= 1
                    if edges_per_node[nei] == 1:
                        q.append(nei)
        
        return list(q)

print(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))