from collections import deque
from typing import List


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


print(Solution().minCostClimbingStairs([10,15,20]))