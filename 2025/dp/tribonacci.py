class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n+1)
        def backtrack(n):
            if n == 0:
                return 0
            if n <= 2:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = backtrack(n-1) + backtrack(n-2) + backtrack(n-3)
            return dp[n]
        return backtrack(n)