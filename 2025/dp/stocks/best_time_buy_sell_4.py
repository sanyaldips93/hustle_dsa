from typing import List


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k+1) for i in range(2)] for i in range(n+1)]

        for ind in range(n-1,-1,-1):
            for buy in [0,1]:
                for cap in range(1,k+1):
                    if buy:
                        dp[ind][buy][cap] = max(-prices[ind]+dp[ind+1][0][cap], dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(prices[ind]+dp[ind+1][1][cap-1], dp[ind+1][0][cap])
        return dp[0][1][k]
    
class Solution2:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (k+1) for i in range(2)]

        for ind in range(n-1,-1,-1):
            temp = [[0] * (k+1) for i in range(2)]
            for buy in [0,1]:
                for cap in range(1,k+1):
                    if buy:
                        temp[buy][cap] = max(-prices[ind]+dp[0][cap], dp[1][cap])
                    else:
                        temp[buy][cap] = max(prices[ind]+dp[1][cap-1], dp[0][cap])
            dp = temp
        return dp[1][k]
    
# All of the below can be applied to III

class Solution3:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * (2*k) for i in range(n)]

        def dfs(ind, trans):
            if trans == (2*k) or ind == n: return 0
            if dp[ind][trans] != -1: return dp[ind][trans]
            if trans % 2 == 0:
                dp[ind][trans] = max(-prices[ind]+dfs(ind+1,trans+1), dfs(ind+1,trans))
            else:
                dp[ind][trans] = max(prices[ind]+dfs(ind+1,trans+1), dfs(ind+1,trans))
            return dp[ind][trans]
        
        return dfs(0,0)

class Solution4:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (2*k+1) for i in range(n+1)]

        for ind in range(n-1,-1,-1):
                for cap in range(2*k-1, -1, -1):
                    if cap % 2 == 0:
                        dp[ind][cap] = max(-prices[ind]+dp[ind+1][cap+1], dp[ind+1][cap])
                    else:
                        dp[ind][cap] = max(prices[ind]+dp[ind+1][cap+1], dp[ind+1][cap])
        return dp[0][0]

class Solution5:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (2*k+1)

        for ind in range(n-1,-1,-1):
            temp = [0] * (2*k+1)
            for cap in range(2*k-1, -1, -1):
                if cap % 2 == 0:
                    temp[cap] = max(-prices[ind]+dp[cap+1], dp[cap])
                else:
                    temp[cap] = max(prices[ind]+dp[cap+1], dp[cap])
            dp = temp
        return dp[0]