import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max = []
        min = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min)

        for i in range(k):
            while min and min[0][0] <= w:
                c, p = heapq.heappop(min)
                heapq.heappush(max, -1 * p)
            if not max:
                break
            w += -1 * heapq.heappop(max)
        return w