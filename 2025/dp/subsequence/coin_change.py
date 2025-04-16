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