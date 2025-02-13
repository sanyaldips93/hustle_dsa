from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = defaultdict(int)
        for i, c in enumerate(s):
            hash[c] = i
        start, end = 0, 0
        res, size = [], 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, hash[c])

            if i == end:
                res.append(size)
                size = 0
        return res