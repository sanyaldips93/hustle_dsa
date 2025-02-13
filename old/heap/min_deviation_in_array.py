import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # T.C -> O(nlogm) : where n is the size of array
        # and logm is the time till which a number can be reduced as possible.
        heapMax, heap = 0, []
        for n in nums:
            tmp = n
            while n % 2 == 0:
                n = n // 2
            heap.append((n, max(tmp, 2*n)))
            heapMax = max(heapMax, n)
        
        # T.C -> O(nlogn * logm) : n is the size of entries, and logn is the as much popping we can do from the heap
        # logm is the number of times a value can be sent back to the heap
        heapq.heapify(heap)
        res = float("inf")
        while len(heap) == len(nums):
            n, nMax = heapq.heappop(heap)
            res = min(res, heapMax - n)

            if n < nMax:
                heapq.heappush(heap, (n * 2, nMax))
                heapMax = max(heapMax, n * 2)

        return res