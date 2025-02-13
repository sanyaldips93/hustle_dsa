from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == dst:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1
        
        return [bfs(src, dst) for src, dst in queries]

        