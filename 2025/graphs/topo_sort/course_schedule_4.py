from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[False]* numCourses for _ in range(numCourses)]

        for u,v in prerequisites:
            dist[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if dist[i][k] and dist[k][j]:
                        dist[i][j] = True
        
        return [dist[u][v] for u, v in queries]
    
print(Solution().checkIfPrerequisite(3, [], [[1,0],[1,2]]))