from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}
        def backtrack(i):
            if i == len(s):
                return True
            if i in dp: return dp[i]
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet and backtrack(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        res = backtrack(0)
        print(dp)
        return res

print(Solution().wordBreak('leetcode', ["leet","cod"]))