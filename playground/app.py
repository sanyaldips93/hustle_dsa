from collections import defaultdict, deque
from typing import List

class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[n-1])

        if n == 1 and m == 1:
            return triangle[n-1][m-1]

        dp = [[-1] * m for _ in range(n)]
        
        for j in range(n-1):
            dp[n-1][j] = triangle[n-1][j]
        
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                d = dp[i+1][j] + triangle[i][j]
                dg = dp[i+1][j+1] + triangle[i][j]
                dp[i][j] = min(d, dg)
        
        return dp[0][0]

print(Solution2.minimumTotal([[1],[2,3]]))