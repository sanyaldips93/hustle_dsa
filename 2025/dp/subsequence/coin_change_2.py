from typing import List


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n)]
        
        def dfs(i, cur):
            if cur == 0: return 1
            if i < 0 or cur < 0: return 0
            if dp[i][cur] != -1: return dp[i][cur]

            np = dfs(i-1,cur)
            p = 0
            if coins[i] <= cur:
                p = dfs(i,cur-coins[i])
            dp[i][cur] = p + np
            return dp[i][cur]
        
        return dfs(n-1,amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n)]
        
        for r in range(n):
            dp[r][0] = 1
        for tar in range(amount+1):
            if tar % coins[0] == 0:
                dp[0][tar] = 1
        
        for r in range(1,n):
            for tar in range(amount+1):
                dp[r][tar] = dp[r-1][tar] + (dp[r][tar-coins[r]] if coins[r] <= tar else 0)
        
        return dp[n-1][amount]
print(Solution().change(5,[1,2,5]))

class Solution3:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        
        dp[0] = 1
        for tar in range(amount+1):
            if tar % coins[0] == 0:
                dp[tar] = 1
        
        for r in range(1,n):
            for tar in range(amount+1):
                dp[tar] = dp[tar] + (dp[tar-coins[r]] if coins[r] <= tar else 0)
        
        return dp[amount]
    
class Solution4:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for tar in range(coin, amount+1):
                dp[tar] += dp[tar-coin]
        
        return dp[amount]