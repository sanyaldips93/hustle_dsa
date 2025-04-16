from typing import List

# Memoization
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[-1] * n for _ in range(n)]

        def dfs(r,c,last):
            if c < 0 or c >= n or c == last:
                return float("inf")
            if r == n-1:
                return grid[r][c]
            if dp[r][c] != -1:
                return dp[r][c]
            val = float("inf")
            for i in range(n):
                val = min(val, dfs(r+1, i, c))
            val += grid[r][c]
            dp[r][c] = val
            return dp[r][c]
        
        res = float("inf")
        for i in range(n):
            res = min(res, dfs(0,i,-1))
        return res

# Tabulation
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float("inf")] * n for _ in range(n)]

        for c in range(n):
            dp[0][c] = grid[0][c]

        for r in range(1,n):
            for c in range(n):
                for dc in range(n):
                    if c != dc:
                        dp[r][c] = min(dp[r][c], grid[r][c] + dp[r-1][dc])
        
        print(dp)
        return min(dp[n-1])

# Space Optimisation
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [-1] * n

        for c in range(n):
            dp[c] = grid[0][c]

        for r in range(1,n):
            temp = [float("inf")] * n
            for c in range(n):
                for dc in range(n):
                    if c != dc:
                        temp[c] = min(temp[c], grid[r][c]+ dp[dc])
            dp = temp
        
        return min(dp)