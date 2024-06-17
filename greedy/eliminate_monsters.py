import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minr = []
        for d, s in zip(dist, speed):
            minr.append(math.ceil(d/s))
        minr.sort()
        res = 0
        for min in range(len(dist)):
            if min >= minr[min]:
                return res
            res += 1
        return res