class Solution:
    def frogJump(self, height, k):
        n = len(height)
        if n == 1: return 0
        dp = [float("inf")] * n
        dp[0] = 0
        dp[1] = abs(height[0] - height[1])

        for i in range(2,n):
            for j in range(1,k+1):
                if abs(i-j) >= 0:
                    dp[i] = min(dp[i], dp[i-j]+abs(height[i-j]-height[i]))
        
        return dp[n-1]