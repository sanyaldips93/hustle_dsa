from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n
        def dfs(i):
            if i == n: return 0
            if dp[i] != -1: return dp[i]
            maxval, maxcost = 0, 0
            for j in range(i,min(i+k, n)):
                maxval = max(maxval, arr[j])
                cost = maxval * (j-i+1) + dfs(j+1)
                maxcost = max(maxcost, cost)
            dp[i] = maxcost
            return maxcost
        return dfs(0)

Solution().maxSumAfterPartitioning([1],1)

# Tabulation

class Solution2:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        for i in range(n-1,-1,-1):
            maxval, maxcost = 0, 0
            for j in range(i,min(i+k, n)):
                maxval = max(maxval, arr[j])
                cost = maxval * (j-i+1) + dp[j+1]
                maxcost = max(maxcost, cost)
            dp[i] = maxcost
        return dp[0]
