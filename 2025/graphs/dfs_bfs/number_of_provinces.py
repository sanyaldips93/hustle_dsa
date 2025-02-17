from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        n = len(isConnected)
        visited = [0] * n
        count = 0

        def dfs(node):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = 1
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                count += 1
                dfs(i)
        
        return count