class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [-1] * n
        def dfs(n):
            if n <= 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            dp[n] = float("inf")
            for i in range(1,k+1):
                if n - i >= 0:
                    dp[n] = min(dp[n], abs(arr[n]-arr[n-i])+dfs(n-i))
            return dp[n]
        return dfs(n-1)

# Tablutation

class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(1,n):
            for j in range(1,k+1):
                if i-j >= 0:
                    dp[i] = min(dp[i], abs(arr[i]-arr[i-j])+dp[i-j])
        return dp[n-1]