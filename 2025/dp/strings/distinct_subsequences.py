class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[-1] * (n+1) for _ in range(m+1)]

        def dfs(i, j):
            if j<0: return 1
            if i<0: return 0
            if dp[i][j] != -1: return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = dfs(i-1,j-1) + dfs(i-1,j)
            else:
                dp[i][j] = dfs(i-1,j)
            return dp[i][j]
        
        return dfs(m-1,n-1)
    


class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for r in range(m+1):
            dp[r][0] = 1 # for target string as empty, we will always have a result of 1
        

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[m][n]
    
class Solution3:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [0] * (n+1)
        dp[0] = 1 # for target string as empty, we will always have a result of 1
        

        for i in range(1,m+1):
            temp = [0] * (n+1)
            temp[0] = 1 # for target string as empty, we will always have a result of 1
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    temp[j] = dp[j-1] + dp[j]
                else:
                    temp[j] = dp[j]
            dp = temp
        return dp[n]
    
class Solution4:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [0] * (n+1)
        dp[0] = 1
        

        for i in range(1,m+1):
            for j in range(n,0,-1): # can choose a character only once.
                if s[i-1] == t[j-1]:
                    dp[j] = dp[j-1] + dp[j]
                else:
                    dp[j] = dp[j]
        return dp[n]