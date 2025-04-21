class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]

        m = len(s)

        dp = [[0] * (m+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # length of string - lcs
        res = m - dp[m][m]
        return res