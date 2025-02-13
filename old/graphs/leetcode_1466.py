from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a,b) for a,b in connections }
        neighbors = { city:[] for city in range(n) }
        visit = set()
        count = 0

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal count
            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                if (neighbor, city) not in edges:
                    count += 1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)   
        dfs(0)
        return count
