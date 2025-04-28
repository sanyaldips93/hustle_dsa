from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add 0 at start and n at end to represent stick endpoints
        # Sort cuts to process them in order
        cuts = [0] + sorted(cuts) + [n]

        def dfs(i, j):
            # Base case: if left index > right index, no valid cuts possible
            if i > j: return 0
            
            # Initialize minimum cost to infinity
            mini = float("inf")
            
            # Try each possible cut position between i and j
            for k in range(i, j+1):
                # Calculate cost for current cut:
                # 1. Length of current segment (cuts[j+1] - cuts[i-1])
                # 2. Cost of cuts in left segment (dfs(i,k-1))
                # 3. Cost of cuts in right segment (dfs(k+1,j))
                cost = cuts[j+1] - cuts[i-1] + dfs(i,k-1) + dfs(k+1,j)
                
                # Update minimum cost if current cost is smaller
                mini = min(mini, cost)
            return mini

        # Start with indices 1 to len(cuts)-2 since 0 and n are not actual cuts
        return dfs(1, len(cuts)-2)
    
# Memoization
class Solution2:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[-1] * (m) for _ in range(m)]
        def dfs(i,j):
            if i>j: return 0
            if dp[i][j] != -1: return dp[i][j]
            mini = float("inf")
            for k in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + dfs(i,k-1) + dfs(k+1,j)
                mini = min(mini, cost)
            dp[i][j] = mini
            return dp[i][j]
        return dfs(1,len(cuts)-2)