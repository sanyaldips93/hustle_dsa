class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r = len(text1)
        c = len(text2)

        dp = [[-1] * c for _ in range(r)]

        def dfs(i,j):
            if i < 0 or j < 0: return 0
            if dp[i][j] != -1: return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i-1,j-1)
            else:
                dp[i][j] = max(dfs(i-1,j), dfs(i,j-1))
            return dp[i][j]
        
        return dfs(r-1, c-1)

# Shifting of index
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r = len(text1)
        c = len(text2)

        dp = [[-1] * (c+1) for _ in range(r+1)]

        def dfs(i,j):
            if i == 0 or j == 0: return 0
            if dp[i][j] != -1: return dp[i][j]

            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dfs(i-1,j-1)
            else:
                dp[i][j] = max(dfs(i-1,j), dfs(i,j-1))
            return dp[i][j]
        
        return dfs(r, c)
    

# Tabulation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r = len(text1)
        c = len(text2)

        dp = [[0] * (c+1) for _ in range(r+1)]

        for i in range(r): dp[i][0] = 0
        for j in range(c): dp[0][j] = 0

        for i in range(1,r+1):
            for j in range(1,c+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[r][c]
    
# Space Optimisation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r = len(text1)
        c = len(text2)
        dp = [0] * (c+1)
        for i in range(1,r+1):
            temp = [0] * (c+1)
            for j in range(1,c+1):
                if text1[i-1] == text2[j-1]:
                    temp[j] = 1 + dp[j-1]
                else:
                    temp[j] = max(dp[j], temp[j-1])
            dp = temp
        
        return dp[c]