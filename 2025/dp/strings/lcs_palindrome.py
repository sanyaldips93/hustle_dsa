class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        n, m = len(s), len(s2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for r in range(1,n+1):
            for c in range(1,m+1):
                if s[r-1] == s2[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return dp[n][m]