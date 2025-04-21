class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        reslen = m + n - dp[m][n]
        s = [""] * reslen
        ind = reslen
        i, j = m, n

        while i>0 and j>0:
            if str1[i-1] == str2[j-1]:
                s[ind-1] = str1[i-1]
                i, j = i-1, j-1
            elif dp[i-1][j] > dp[i][j-1]:
                s[ind-1] = str1[i-1]
                i = i-1
            else:
                s[ind-1] = str2[j-1]
                j = j-1
            ind = ind-1
        
        while i>0:
            s[ind-1] = str1[i-1]
            i, ind = i-1, ind-1
        
        while j>0:
            s[ind-1] = str2[j-1]
            j, ind = j-1, ind-1
        
        return "".join(s)