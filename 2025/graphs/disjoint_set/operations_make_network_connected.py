from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if rank[px] > rank[py]:
                par[py] = px
            elif rank[px] < rank[py]:
                par[px] = py
            else:
                par[px] = py
                rank[py] += 1
        
        extraedges = 0
        for u,v in connections:
            if find(u) == find(v):
                extraedges += 1
            else:
                union(u, v)
        
        components = 0
        for i in range(n):
            if par[i] == i:
                components += 1
        
        if extraedges >= components - 1:
            return components - 1
        
        return -1

print(Solution().makeConnected(4, [[0,1],[0,2],[1,2]]))