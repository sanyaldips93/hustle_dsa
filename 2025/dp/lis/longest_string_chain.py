from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        dp = [1] * n
        words.sort(key=len)
        maxi = 0
        for i in range(n):
            for prev in range(i):
                if self.compare(words[i], words[prev]) and 1+dp[prev] > dp[i]:
                    dp[i] = max(dp[i], 1+dp[prev])
            maxi = max(maxi, dp[i])
        return maxi
    
    def compare(self, word1, word2):
        if len(word1) != len(word2)+1:
            return False
        first, second = 0,0
        while first < len(word1):
            if second < len(word2) and word1[first] == word2[second]:
                second = second+1
            first = first+1
        return first == len(word1) and second == len(word2)