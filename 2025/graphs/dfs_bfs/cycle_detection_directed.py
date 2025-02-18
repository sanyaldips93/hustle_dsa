from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an directed graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visit = set()
        recurse = set()
        
        def dfs(i):
            visit.add(i)
            recurse.add(i)
            for nei in adj[i]:
                if nei not in visit and dfs(nei):
                    return True
                if nei in recurse:
                    return True
            recurse.remove(i)
            return False

        
        for i in range(V):
            if i not in visit and dfs(i):
                return True
        
        return False  # No cycle found
    
print(Solution().isCycle(3, [[1], [2], []]))