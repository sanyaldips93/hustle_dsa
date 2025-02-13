from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        used = set()
        res = 0
        for c, freq in count.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res