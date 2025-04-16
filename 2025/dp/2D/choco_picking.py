
# Memoization
from typing import List


class Solution:
    def solve(self, n, m, grid):
        # Code here
        dp = [[[-1] * m for i in range(m)] for k in range(n)]
        def dfs(i, j1, j2):
            if j1 < 0 or j2 < 0 or j1 >= m or j2 >= m:
                return float("-inf")
            if i == n-1:
                if j1==j2:
                    return grid[i][j2]
                else:
                    return grid[i][j1] + grid[i][j2]
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            
            maxi = float("-inf")
            for dj1 in range(-1, 2):
                for dj2 in range(-1, 2):
                    val = 0
                    if j1==j2:
                        val += grid[i][j1]
                    else:
                        val += grid[i][j1] + grid[i][j2]
                    val += dfs(i+1, j1+dj1, j2+dj2)
                    maxi = max(maxi, val)
            dp[i][j1][j2] = maxi
            return dp[i][j1][j2]
        
        return dfs(0,0,m-1)

# Tabulation

class Solution:
    def solve(self, n, m, grid):
        # Code here
        dp = [[[-1] * m for i in range(m)] for k in range(n)]
        
        for j1 in range(m):
            for j2 in range(m):
                if j1==j2:
                    dp[n-1][j1][j2] = grid[n-1][j2]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float("-inf")
                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):
                            val = 0
                            if j1==j2:
                                val = grid[i][j2]
                            else:
                                val = grid[i][j1] + grid[i][j2]
                            if j1+dj1 >= 0 and j2+dj2 >= 0 and j1+dj1 < m and j2+dj2 < m:
                                val += dp[i+1][j1+dj1][j2+dj2]
                            else:
                                val = 0
                            maxi = max(maxi, val)
                    dp[i][j1][j2] = maxi
        
        return dp[0][0][m-1]
    
# Space Optimisation
class Solution:
    def solve(self, n, m, grid):
        # Step 1: Initialize 3D DP table
        dp = [[0] * m for _ in range(m)]

        # Step 2: Base Case - Fill last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[j1][j2] = grid[n-1][j1]
                else:
                    dp[j1][j2] = grid[n-1][j1] + grid[n-1][j2]

        # Step 3: Fill DP table bottom-up
        for i in range(n-2, -1, -1):  # From second last row to first row
            temp = [[0] * m for _ in range(m)]
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float("-inf")
                    for dj1 in [-1, 0, 1]:  # Alice moves
                        for dj2 in [-1, 0, 1]:  # Bob moves
                            if 0 <= j1+dj1 < m and 0 <= j2+dj2 < m:
                                value = dp[j1+dj1][j2+dj2]
                                if j1 == j2:
                                    value += grid[i][j1]  # If they meet
                                else:
                                    value += grid[i][j1] + grid[i][j2]  # If different
                                maxi = max(maxi, value)
                    temp[j1][j2] = maxi  # Store max chocolates
            dp = temp

        # Step 4: Return answer from the top row (starting positions)
        return dp[0][m-1]
    


# Neetcode
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = {}
        def dfs(r, c1, c2):
            if min(c1,c2) < 0 or max(c1,c2) >= COLS:
                return 0
            if r == ROWS-1:
                return grid[r][c1] + (grid[r][c2] if c2 != c1 else 0)
            if (r, c1, c2) in dp:
                return dp[(r, c1, c2)]
            
            maxval = 0
            for dc1 in range(-1, 2):
                for dc2 in range(-1, 2):
                    val = 0
                    val += grid[r][c1] + (grid[r][c2] if c2 != c1 else 0)
                    val += dfs(r+1,c1+dc1,c2+dc2)
                    maxval = max(maxval, val)
            dp[(r, c1, c2)] = maxval
            return dp[(r, c1, c2)]
        
        return dfs(0,0,COLS-1)