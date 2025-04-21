from typing import List
class Solution1:
  def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    dp = [[-1] * (w+1) for _ in range(n)]
    def dfs(i, cur):
        if i == 0:
            return cur // weight[0] * profit[0]
        if dp[i][cur] != -1:
            return dp[i][cur]
        np = dfs(i-1, cur)
        p = 0
        if weight[i] <= cur:
            p = dfs(i, cur-weight[i]) + profit[i]
        dp[i][cur] = max(np, p)
        return dp[i][cur]
    return dfs(n-1, w)

class Solution2:
  def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    dp = [[-1] * (w+1) for _ in range(n)]
    for tar in range(w+1):
        dp[0][tar] = tar // weight[0] * profit[0]
    for r in range(1,n):
        for tar in range(w+1):
            np = dp[r-1][tar]
            p = 0
            if weight[r] <= tar:
                p = dp[r][tar-weight[r]] + profit[r]
            dp[r][tar] = max(p, np)
    return dp[n-1][w]
  
class Solution3:
  def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    dp = [-1] * (w+1)
    for tar in range(w+1):
        dp[tar] = tar // weight[0] * profit[0]
    for r in range(1,n):
        for tar in range(w+1):
            np = dp[tar]
            p = 0
            if weight[r] <= tar:
                p = dp[tar-weight[r]] + profit[r]
            dp[tar] = max(p, np)
    return dp[w]
  
