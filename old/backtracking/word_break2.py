from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cur, res = [], []
        wordDict = set(wordDict)
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    cur.append(s[i:j+1])
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return res
    
# print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  # ["cats and dog", "cat sand dog"]


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]

            res = []
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w not in wordDict:
                    continue
                strings = backtrack(j + 1)
                for substr in strings:
                    sentence = w
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
            cache[i] = res
            return res

        return backtrack(0)
    
print(Solution2().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  # ["cats and dog", "cat sand dog"]