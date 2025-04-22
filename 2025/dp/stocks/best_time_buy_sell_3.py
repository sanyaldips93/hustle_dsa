from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1] * 3 for i in range(2)] for i in range(n)]

        def dfs(ind, buy, cap):
            if cap == 0 or ind == n: return 0
            if dp[ind][buy][cap] != -1: return dp[ind][buy][cap]
            if buy:
                dp[ind][buy][cap] = max(-prices[ind]+dfs(ind+1,0,cap), dfs(ind+1,1,cap))
            else:
                dp[ind][buy][cap] = max(prices[ind]+dfs(ind+1,1,cap-1), dfs(ind+1,0,cap))
            return dp[ind][buy][cap]
        
        return dfs(0,1,2)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 3 for i in range(2)] for i in range(n+1)]

        for ind in range(n-1,-1,-1):
            for buy in [0,1]:
                for cap in [1,2]:
                    if buy:
                        dp[ind][buy][cap] = max(-prices[ind]+dp[ind+1][0][cap], dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(prices[ind]+dp[ind+1][1][cap-1], dp[ind+1][0][cap])
        return dp[0][1][2]
    

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 3 for i in range(2)]

        for ind in range(n-1,-1,-1):
            temp = [[0] * 3 for i in range(2)]
            for buy in [0,1]:
                for cap in [1,2]:
                    if buy:
                        temp[buy][cap] = max(-prices[ind]+dp[0][cap], dp[1][cap])
                    else:
                        temp[buy][cap] = max(prices[ind]+dp[1][cap-1], dp[0][cap])
            dp = temp
        return dp[1][2]