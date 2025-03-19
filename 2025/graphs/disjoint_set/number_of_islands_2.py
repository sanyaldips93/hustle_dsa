from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        n = rows * cols
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
            
            if px == py:
                return False
            
            if rank[px] > rank[py]:
                par[py] = px
            elif rank[py] > rank[px]:
                par[px] = py
            else:
                par[py] = px
                rank[px] += 1
            return True
        
        res = []
        visit = set()
        count = 0
        
        for r,c in operators:
            if (r,c) in visit:
                res.append(count)
                continue
            visit.add((r,c))
            count += 1
            for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                nr = dr+r
                nc = dc+c
                if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) not in visit:
                    continue
                node = r * cols + c
                newnode = nr * cols + nc
                if union(node, newnode):
                    count -= 1
            res.append(count)
        
        return res

print(Solution().numOfIslands(4, 5, [[1,1],[0,1],[3,3],[3,4]]))