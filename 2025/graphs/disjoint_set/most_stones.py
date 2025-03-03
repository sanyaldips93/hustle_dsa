from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        maxRows, maxCols = 0, 0
        for row, col in stones:
            maxRows = max(maxRows, row)
            maxCols = max(maxCols, col)
        
        n = maxRows + maxCols + 2
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

            if px != py:
                if rank[px] > rank[py]:
                    par[py] = px
                elif rank[py] > rank[px]:
                    par[px] = py
                else:
                    par[py] = px
                    rank[px] += 1

        stoneNodes = {}
        for u,v in stones:
            row = u
            col = v + maxRows + 1
            union(row, col)
            stoneNodes[row] = 1
            stoneNodes[col] = 1
        
        components = 0
        for i in stoneNodes:
            if i == find(i):
                components += 1
        
        return len(stones) - components
    

print(Solution().removeStones([[0,1],[1,1]]))