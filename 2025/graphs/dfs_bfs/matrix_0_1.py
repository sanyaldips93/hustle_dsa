from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        visit = set()

        directions = [[0,1], [1,0], [0,-1], [-1,0]]
            
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c, 0])
                else:
                    mat[r][c] = -1
        
        while q:
            r, c, val = q.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    mat[nr][nc] = val+1
                    visit.add((nr, nc))
                    q.append([nr, nc, val+1])

        return mat
    
print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))