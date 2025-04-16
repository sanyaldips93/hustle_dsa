# Memoization
class Solution2:
    def knapsack(self, n, wei, val, W):
        dp = [[0] * (W+1) for _ in range(n)]

        def dfs(i, wt):
            if i == 0:
                return val[0] if wei[0] <= wt else 0

            if dp[i][wt] != 0:
                return dp[i][wt]
            
            np = 0 + dfs(i-1, wt)
            p = 0
            if wei[i] <= wt:
                p = val[i] + dfs(i-1, wt-wei[i])
            
            dp[i][wt] = max(np, p)
            return dp[i][wt]
        
        return dfs(n-1, W)
print(Solution2().knapsack(2, [2,3], [30,40], 4))


# Tabulation
class Solution:
    def knapsack(self, n, wei, val, W):
        dp = [[0] * (W+1) for _ in range(n)]

        for j in range(wei[0], W+1):
            dp[0][j] = val[0]
        
        for r in range(1,n):
            for tar in range(W+1):
                np = dp[r-1][tar] + 0
                p = 0
                if wei[r] <= tar:
                    p = val[r] + dp[r-1][tar-wei[r]]
                dp[r][tar] = max(p, np)
        
        return dp[n-1][W]
# print(Solution().knapsack(3, [2,3,4], [30,40,50], 5))

# Space Optimisation
class Solution3:
    def knapsack(self, n, wei, val, W):
        dp = [0] * (W+1)

        for j in range(wei[0], W+1):
            dp[j] = val[0]
        
        for r in range(1,n):
            temp = [0] * (W+1)
            for tar in range(W+1):
                np = dp[tar] + 0
                p = 0
                if wei[r] <= tar:
                    p = val[r] + dp[tar-wei[r]]
                temp[tar] = max(p, np)
            dp = temp
        
        return dp[W]
print(Solution3().knapsack(3, [2,3,4], [30,40,50], 5))

# Single Array DP
class Solution4:
    def knapsack(self, n, wei, val, W):
        dp = [0] * (W+1)

        for r in range(n):
            for tar in range(wei[r], W+1):
                dp[tar] = max(dp[tar], val[r]+dp[tar-wei[r]])
        
        return dp[W]
print(Solution4().knapsack(3, [2,3,4], [30,40,50], 5))