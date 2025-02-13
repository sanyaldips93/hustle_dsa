# Minimum Fuel Cost to Report to the Capital

from ast import List
from collections import defaultdict
from math import ceil


class Solution:
    def minimumFuelCost(self, roads, seats):
        adj = defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)
        def dfs(node, prev):
            passengers = 0
            nonlocal res
            for child in adj[node]:
                if child != prev:
                    p = dfs(child, node)
                    passengers += p
                    res += int(ceil(p / seats))
            return passengers + 1
        res = 0
        dfs(0, -1)
        return res
    
print(Solution().minimumFuelCost([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2))