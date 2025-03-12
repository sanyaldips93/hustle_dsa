class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev, prev1 = 1, 1
        for i in range(2,n+1):
            cur = prev + prev1
            prev = prev1
            prev1 = cur
        return prev1
    
    def climbStairs2(self, n: int) -> int:
        dp = [-1] * (n+1)
        def dfs(n):
            if n <= 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2)
            return dp[n]
        return dfs(n)

print(Solution().climbStairs2(2))