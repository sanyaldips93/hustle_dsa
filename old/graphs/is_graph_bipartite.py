from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)
        def bfs(i):
            if color[i]:
                return True
            q = deque([i])
            color[i] = -1
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if color[nei] == color[i]:
                        return False
                    elif not color[nei]:
                        q.append(nei)
                        color[nei] = -1 * color[i]
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
    
print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))