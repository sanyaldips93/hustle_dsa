from collections import defaultdict, deque
from typing import List

# Play with your code
from typing import List
from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * m for _ in range(n)]

        def dfs(i, j):
            if i == 0 and j == 0: return grid[i][j]
            if i < 0 or j < 0: return float('inf')
            if dp[i][j] != float("inf"): return dp[i][j]
            dp[i][j] = min(dfs(i-1, j), dfs(i, j-1)) + grid[i][j]
            return dp[i][j]
        return dfs(m-1, n-1)

print(Solution().minPathSum([[1,2,3],[4,5,6]]))