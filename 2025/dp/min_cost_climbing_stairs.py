from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])


# Memoization

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        def dfs(n):
            if n <= 1:
                return cost[n]
            if dp[n] != -1:
                return dp[n]
            dp[n] = cost[n] + min(dfs(n-1), dfs(n-2))
            return dp[n]
        
        return min(dfs(n-1), dfs(n-2))