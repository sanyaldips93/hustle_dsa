from typing import List

# Memoization
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1] * m for _ in range(n)]
        def dfs(r, c):
            if r >= 0 and c >= 0 and obstacleGrid[r][c] == 1:
                return 0
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            
            up = dfs(r-1, c)
            left = dfs(r, c-1)
            dp[r][c] = up + left
            return dp[r][c]
        
        return dfs(n-1, m-1)
    
# Tabulation
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if r >= 0 and c >= 0 and obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                if r == 0 and c == 0:
                    dp[r][c] = 1
                    continue
                up, left = 0, 0
                if r > 0:
                    up = dp[r-1][c]
                if c > 0:
                    left = dp[r][c-1]
                
                dp[r][c] = up + left
        return dp[n-1][m-1]

# Space Optimisation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0] * m
        for r in range(n):
            temp = [0] * m
            for c in range(m):
                if r >= 0 and c >= 0 and obstacleGrid[r][c] == 1:
                    temp[c] = 0
                    continue
                if r == 0 and c == 0:
                    temp[c] = 1
                    continue
                up, left = 0, 0
                if c > 0:
                    left = temp[c-1]
                up = dp[c]
                
                temp[c] = up + left
            dp = temp
        return dp[m-1]