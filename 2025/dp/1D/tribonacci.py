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
    
# Space Optimisation
class Solution:
    def tribonacci(self, n: int) -> int:
        p1, p2, p3 = 0, 1, 1
        if n == 0:
            return p1
        for i in range(3, n+1):
            cur = p1 + p2 + p3
            p1 = p2
            p2 = p3
            p3 = cur
        return p3