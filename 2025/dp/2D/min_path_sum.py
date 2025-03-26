from typing import List

# Memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[-1] * m for _ in range(n)]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            if r == 0 and c == 0:
                return grid[r][c]
            if r < 0 or c < 0:
                return float("inf")
            
            up = dfs(r-1, c)
            left = dfs(r, c-1)

            dp[r][c] = min(up, left) + grid[r][c]
            return dp[r][c]
        
        return dfs(n-1, m-1)
    
# Tabulation
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[-1] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                    continue
                up, left = float("inf"), float("inf")
                if r > 0:
                    up = dp[r-1][c]
                if c > 0:
                    left = dp[r][c-1]
                dp[r][c] = min(up, left) + grid[r][c]
        
        return dp[n-1][m-1]
    
# Space Optimisation
class Solution3:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [-1] * m

        for r in range(n):
            temp = [-1] * m
            for c in range(m):
                if r == 0 and c == 0:
                    temp[c] = grid[r][c]
                    continue
                up, left = float("inf"), float("inf")
                if r > 0:
                    up = dp[c]
                if c > 0:
                    left = temp[c-1]
                temp[c] = min(up, left) + grid[r][c]
            dp = temp
        
        return dp[m-1]
            