class Solution:
    def topDown(self, n):
        if n <= 1:
            return n
        prev = 1
        prev2 = 0
        for i in range(2,n):
            cur = prev + prev2
            prev2 = prev
            prev = cur
        return prev
            
    def bottomUp(self, n):
        dp = [-1] * (n+1)
        def dfs(n):
            if n <= 1:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2)
            return dp[n]
        dfs(n)
        return dp[n]