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
            
        
        reslen = dp[r][c]
        s = [""] * reslen
        index = reslen

        i, j = r, c
        while i > 0 and j > 0 and index >= 0:
            if text1[i-1] == text2[j-1]:
                s[index-1] = text1[i-1]
                index -= 1
                i, j = i-1, j-1
            elif dp[i-1][j] > dp[i][j-1]:
                i = i-1
            else:
                j = j-1
        
        return "".join(s)

print(Solution().longestCommonSubsequence("abcde", "bdgek"))