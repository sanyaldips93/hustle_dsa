import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        kinv = len(nums) - k + 1
        minheap = [int(i) for i in nums]
        heapq.heapify(minheap)
        while kinv > 1:
            heapq.heappop(minheap)
            kinv -= 1
        return str(heapq.heappop(minheap))

print(Solution().kthLargestNumber(["2","21","12","1"], 3))