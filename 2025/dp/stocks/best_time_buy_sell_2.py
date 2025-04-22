from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        def dfs(i, buy):
            if i == n: return 0
            if dp[i][buy] != -1: return dp[i][buy]
            profit = 0
            if buy:
                dp[i][buy] = max(-prices[i]+dfs(i+1,0), dfs(i+1,1))
            else:
                dp[i][buy] = max(prices[i]+dfs(i+1,1), dfs(i+1,0))
            return dp[i][buy]
        return dfs(0, 1)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for j in [0,1]:
                if j:
                    dp[i][j] = max(-prices[i]+dp[i+1][0], dp[i+1][1])
                else:
                    dp[i][j] = max(prices[i]+dp[i+1][1], dp[i+1][0])
        return dp[0][1] 



class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * 2
        
        for i in range(n-1,-1,-1):
            temp = [0] * 2
            for j in [0,1]:
                if j:
                    temp[j] = max(-prices[i]+dp[0], dp[1])
                else:
                    temp[j] = max(prices[i]+dp[1], dp[0])
            dp = temp
            
class Solution4: # Greedy
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prev:
                profit += prices[i]-prev
            prev = prices[i]
        return profit