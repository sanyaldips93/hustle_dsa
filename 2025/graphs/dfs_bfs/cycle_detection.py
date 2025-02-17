from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visit = set()
        
        def bfs(start):
            q = deque([(start, -1)])  # Initialize queue inside BFS
            
            while q:
                node, par = q.popleft()
                visit.add(node)
                
                for nei in adj[node]:
                    if nei not in visit:
                        q.append((nei, node))
                    elif nei != par:  # Correct cycle condition
                        return True
            return False
        
        def dfs(i, parent):
            visit.add(i)
            for nei in adj[i]:
                if nei not in visit:
                    if dfs(nei, i):
                        return True
                elif nei != parent:
                    return True
            return False
        
        # Run BFS for every component
        for i in range(V):
            if i not in visit:
                if bfs(i): # or use dfs(i, -1)
                    return True  # Cycle detected
        
        return False  # No cycle found