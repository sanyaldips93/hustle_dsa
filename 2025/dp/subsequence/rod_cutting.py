# Memoization
class Solution:
  def cutRod(price, n):
    dp = [[-1] * (n+1) for _ in range(n)]
    def dfs(i, cur):
        if i == 0:
            return price[0] * cur
        if dp[i][cur] != -1:
            return dp[i][cur]
        np = dfs(i-1,cur)
        p = float("-inf")
        if i+1 <= cur:
            p = dfs(i,cur-i-1) + price[i]
        dp[i][cur] = max(p, np)
        return dp[i][cur]
    return dfs(n-1, n)

# Tabulation
class Solution2:
  def cutRod(price, n):
    dp = [[0] * (n+1) for _ in range(n)]
    for c in range(1,n+1):
        if c % 1 == 0:
            dp[0][c] = (c // 1) * price[0]
    for r in range(n):
        for tar in range(n+1):
            np = dp[r-1][tar]
            p = 0
            if r+1 <= tar:
                p = dp[r][tar-r-1] + price[r]
            dp[r][tar] = max(p, np)
    return dp[n-1][n]
    
  
class Solution3:
  def cutRod(price, n):
    dp = [0] * (n+1)
    for c in range(1,n+1):
        if c % 1 == 0:
            dp[c] = (c // 1) * price[0]
    for r in range(n):
        for tar in range(n+1):
            np = dp[tar]
            p = 0
            if r+1 <= tar:
                p = dp[tar-r-1] + price[r]
            dp[tar] = max(p, np)
    return dp[n]