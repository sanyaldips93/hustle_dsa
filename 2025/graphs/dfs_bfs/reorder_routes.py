from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a1, a2) for a1, a2 in connections }
        adj = { city: [] for city in range(n) }
        visit = set()
        for a1, a2 in connections:
            adj[a1].append(a2)
            adj[a2].append(a1)

        changes = 0
        def dfs(node):
            nonlocal changes
            for nei in adj[node]:
                if nei not in visit:
                    if (nei, node) not in edges:
                        changes += 1
                    visit.add(nei)
                    dfs(nei)
        
        visit.add(0)
        dfs(0)
        return changes