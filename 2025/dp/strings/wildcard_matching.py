class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[-1] * (n+1) for _ in range(m+1)]
        
        def dfs(i, j):
            if i==0 and j==0: return True
            if j==0: return False
            if i==0 and j>0:
                for k in range(1,j+1):
                    if p[k-1] != "*": return False
                return True
            if dp[i][j] != -1: return dp[i][j]

            if s[i-1] == p[j-1] or p[j-1] == '?':
                dp[i][j] = dfs(i-1, j-1)
            elif p[j-1] == "*":
                dp[i][j] = dfs(i, j-1) or dfs(i-1, j)
            else:
                dp[i][j] = False
            return dp[i][j]
        return dfs(m, n)
    

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0] = True
        for c in range(1,n+1):
            if p[c-1] == "*":
                dp[0][c] = dp[0][c-1]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[m][n]


class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [False] * (n+1)

        dp[0] = True
        for c in range(1,n+1):
            if p[c-1] == "*":
                dp[c] = dp[c-1]

        for i in range(1,m+1):
            temp = [False] * (n+1)
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    temp[j] = dp[j-1]
                elif p[j-1] == "*":
                    temp[j] = temp[j-1] or dp[j]
                else:
                    temp[j] = False
            dp = temp
        return dp[n]