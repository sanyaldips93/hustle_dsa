from typing import List

# Memoization
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1] * n for _ in range(n)]

        def dfs(r, c):
            if r < 0 or c < 0 or r == n or c == n:
                return float("inf")
            if dp[r][c] != -1:
                return dp[r][c]
            if r == n-1:
                return matrix[r][c]
            down = dfs(r+1, c)
            ldg = dfs(r+1, c-1)
            rdg = dfs(r+1, c+1)
            dp[r][c] = min(down, ldg, rdg) + matrix[r][c]
            return dp[r][c]
        
        res = float("inf")
        for i in range(n):
            res = min(res, dfs(0,i))
        
        return res

print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))

# Tabulation
class Solution2:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float("inf")] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if r == 0:
                    dp[r][c] = matrix[r][c]
                    continue
                up, ldg, rdg = float("inf"), float("inf"), float("inf")
                if c > 0:
                    ldg = dp[r-1][c-1]
                if c < n-1:
                    rdg = dp[r-1][c+1]
                up = dp[r-1][c]
                dp[r][c] = min(up, ldg, rdg) + matrix[r][c]
        
        res = float("inf")
        for i in range(n):
            res = min(res, dp[n-1][i])
        return res

# Space Optimisation
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [0] * n

        for r in range(n):
            temp = [float("inf")] * n
            for c in range(n):
                up, ldg, rdg = float("inf"), float("inf"), float("inf")
                if c > 0:
                    ldg = dp[c-1]
                if c < n-1:
                    rdg = dp[c+1]
                up = dp[c]
                temp[c] = min(up, ldg, rdg) + matrix[r][c]
            dp = temp
        
        res = float("inf")
        for i in range(n):
            res = min(res, dp[i])
        return res