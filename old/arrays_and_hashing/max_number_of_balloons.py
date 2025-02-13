from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        b = Counter('balloon')
        res = len(text)
        for ch in b:
            res = min(res, c[ch] // b[ch])
        return res