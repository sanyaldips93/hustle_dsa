class Solution:
    def kosaraju(self, adj):
        # First DFS (Topological Ordering)
        visit = set()
        stack = []
        
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
            stack.append(node)  # Append after visiting all neighbors
        
        for i in range(len(adj)):
            if i not in visit:
                dfs(i)
        
        # Reverse the edges
        readj = {i: [] for i in range(len(adj))}  # Fix: Ensure all nodes exist in readj
        for i in range(len(adj)):
            for neighbor in adj[i]:
                readj[neighbor].append(i)  # Reverse edge direction
        
        # Second DFS (Counting SCCs)
        revisit = set()
        
        def redfs(node):
            revisit.add(node)
            for nei in readj[node]:
                if nei not in revisit:
                    redfs(nei)
        
        scc = 0
        while stack:
            node = stack.pop()  # Process in decreasing order of finish time
            if node not in revisit:
                scc += 1
                redfs(node)
        
        return scc