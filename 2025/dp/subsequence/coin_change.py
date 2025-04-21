from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {}
        def dfs(i, s):

            if s == amount:
                return 0
            if s > amount or i < 0:
                return float("inf")
            if (i,s) in dp:
                return dp[(i,s)]
            
            np = dfs(i-1, s)
            p = 1 + dfs(i, s+coins[i])

            dp[(i,s)] = min(np, p)
            return dp[(i,s)]
        
        res = dfs(n-1, 0)
        return res if res != float("inf") else -1

print(Solution().coinChange([2],3))

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float("inf")] * (amount+1)
        for tar in range(amount+1):
            if tar % coins[0] == 0:
                dp[tar] = tar // coins[0]
        for r in range(1,n):
            for tar in range(coins[r], amount+1):
                dp[tar] = min(dp[tar],dp[tar-coins[r]]+1)
        return dp[amount] if dp[amount] != float("inf") else -1