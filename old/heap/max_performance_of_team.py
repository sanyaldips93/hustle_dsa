import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for s, e in zip(speed, efficiency):
            eng.append([e, s])
        eng.sort(reverse=True)
        heap = []
        res, speed = 0, 0
        for eff, spd in eng:
            if len(heap) == k:
                speed -= heapq.heappop(heap)
            speed += spd
            heapq.heappush(heap, spd)
            res = max(res, eff * speed)
        return res % (10 ** 9 + 7)


print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))