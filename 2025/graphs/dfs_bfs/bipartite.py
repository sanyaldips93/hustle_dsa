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
                node = q.popleft()
                for nei in graph[node]:
                    if color[node] == color[nei]:
                        return False
                    elif not color[nei]:
                        q.append(nei)
                        color[nei] = -1 * color[node]
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
        

class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        def dfs(i, clr):
            color[i] = clr
            for nei in graph[i]:
                if color[i] == color[nei]:
                    return False
                if color[nei] == 0 and not dfs(nei, -clr):
                    return False
            return True
        
        for i in range(len(graph)):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True