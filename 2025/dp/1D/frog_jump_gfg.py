class Solution:
    def minCost(self, height):
        n = len(height)
        if n == 1:
            return 0
        dp = [0] * n
        dp[1] = abs(height[0]-height[1])
        
        for i in range(2, n):
            dp[i] = min(abs(height[i]-height[i-2])+dp[i-2], abs(height[i]-height[i-1])+dp[i-1])
        
        return dp[n-1]

print(Solution().minCost(20,30,10,20))

# Memoization
class Solution2:
    def minCost(self, height):
        # code here
        n = len(height)
        if n == 1:
            return 0
        dp = [-1] * n
        dp[0] = 0
        dp[1] = abs(height[0]-height[1])
        
        def dfs(n):
            if dp[n] != -1:
                return dp[n]
            one = abs(height[n-1]-height[n]) + dfs(n-1)
            two = abs(height[n-2]-height[n]) + dfs(n-2)
            dp[n] = min(one, two)
            return dp[n]
        
        return dfs(n-1)

print(Solution2().minCost(20,30,10,20))