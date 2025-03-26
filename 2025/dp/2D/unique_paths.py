class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def dfs(r, c):
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0 or r == m or c == n:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            up = dfs(r-1, c)
            left = dfs(r, c-1)
            dp[r][c] = up + left
            return dp[r][c]
        return dfs(m-1, n-1)

print(Solution().uniquePaths(3, 7))

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 1
        for c in range(1,n):
            dp[0][c] = 1
        for r in range(1,m):
            dp[r][0] = 1
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]

class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        for r in range(1,m):
            temp = [0] * n
            temp[0] = 1
            for c in range(1,n):
                temp[c] = temp[c-1] + dp[c]
            dp = temp

        return dp[n-1]

class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    temp[i] = 1
                    continue
                up, left = 0, 0
                if i > 0:
                    up = dp[j]
                if j > 0:
                    left = temp[j-1]
                temp[j] = up + left
            dp = temp
        
        return dp[n-1]