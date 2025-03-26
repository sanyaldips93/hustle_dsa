from typing import List

# Memoization
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[n-1])
        dp = [[-1] * m for _ in range(n)]
        def dfs(i,j):
            if i == n-1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            d = triangle[i][j] + dfs(i+1, j)
            dg = triangle[i][j] + dfs(i+1, j+1)

            dp[i][j] = min(d, dg)
            return dp[i][j]
        
        return dfs(0,0)
    
# Tabulation
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[n-1])

        if n == 1 and m == 1:
            return triangle[n-1][m-1]

        dp = [[-1] * m for _ in range(n)]
        
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                d = dp[i+1][j] + triangle[i][j]
                dg = dp[i+1][j+1] + triangle[i][j]
                dp[i][j] = min(d, dg)
        
        return dp[0][0]

print(Solution2().minimumTotal([[1],[2,3]]))


class Solution3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[n-1])

        if n == 1 and m == 1:
            return triangle[n-1][m-1]

        dp = [-1] * n
        
        for j in range(n):
            dp[j] = triangle[n-1][j]
        
        for i in range(n-2, -1, -1):
            temp = [-1] * n
            for j in range(i, -1, -1):
                d = dp[j] + triangle[i][j]
                dg = dp[j+1] + triangle[i][j]
                temp[j] = min(d, dg)
            dp = temp
        
        return dp[0]