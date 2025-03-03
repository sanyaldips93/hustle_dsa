from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        par = [i for i in range(n*n)]
        size = [1] * n * n

        def find(x):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if size[px] >= size[py]:
                par[py] = px
                size[px] = size[py] + size[px]
            else:
                par[px] = py
                size[py] = size[px] + size[py]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                directions = [[0,1], [1,0], [-1,0], [0,-1]]
                node = n * i + j
                for dr, dc in directions:
                    nr = dr + i
                    nc = dc + j
                    newnode = n * nr + nc
                    if min(nr, nc) < 0 or max(nr, nc) == n:
                        continue
                    union(node, newnode) if grid[nr][nc] == 1 else None

        mxval = 0
        for i in range(n):
            for j in range(n):
                visit = set()
                if grid[i][j] == 1:
                    continue
                directions = [[0,1], [1,0], [-1,0], [0,-1]]
                # node = n * i + j
                for dr, dc in directions:
                    nr = dr + i
                    nc = dc + j
                    newnode = n * nr + nc
                    if min(nr, nc) < 0 or max(nr, nc) == n:
                        continue
                    visit.add(find(newnode)) if grid[nr][nc] == 1 else None
                
                val = 0
                for parent in visit:
                    val += size[parent]
                mxval = max(mxval, val+1)
        
        for i in range(n*n):
                mxval = max(mxval, size[par[i]])
        
        return mxval
    
print(Solution().largestIsland([[1,1],[0,1]]))