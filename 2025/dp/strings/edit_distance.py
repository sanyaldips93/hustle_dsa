class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1] * (n) for _ in range(m)]
        
        def dfs(i, j):
            if j < 0: return i+1
            if i < 0: return j+1
            if dp[i][j] != -1: return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = dfs(i-1,j-1)
            else:
                dp[i][j] = 1 + min(dfs(i-1,j-1), dfs(i-1,j), dfs(i,j-1))
            
            return dp[i][j]
        return dfs(m-1, n-1)

# Tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for r in range(m+1):
            dp[r][0] = r
        for c in range(n+1):
            dp[0][c] = c
        
        for r in range(1,m+1):
            for c in range(1,n+1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c-1], min(dp[r-1][c], dp[r][c-1]))
        
        return dp[m][n]
    
# Space Optimisation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [0] * (n+1)
        
        for c in range(n+1):
            dp[c] = c
        
        for r in range(1,m+1):
            temp = [0] * (n+1)
            temp[0] = r # because the first cell of every row indicates, the deletion of that many chars to achieve desired string
            for c in range(1,n+1):
                if word1[r-1] == word2[c-1]:
                    temp[c] = dp[c-1]
                else:
                    temp[c] = 1 + min(dp[c-1], min(dp[c], temp[c-1]))
            dp = temp
        
        return dp[n]