
from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]):
        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()
        visit = set()

        def addroom(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or rooms[r][c] == -1 or (r, c) in visit:
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(rows):
          for c in range(cols):
            if rooms[r][c] == 0:
               q.append([r, c])
               visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
              [r, c] = q.popleft()
              rooms[r][c] = dist
              addroom(r+1, c)
              addroom(r-1, c)
              addroom(r, c+1)
              addroom(r, c-1)
        
            dist += 1

        return rooms
        
print(Solution().wallsAndGates([[2147483647,-1,0,2147483647],
                                [2147483647,2147483647,2147483647,-1],
                                [2147483647,-1,2147483647,-1],
                                [0,-1,2147483647,2147483647]]
                              ))
              
