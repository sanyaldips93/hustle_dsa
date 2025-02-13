from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax, globalmin = nums[0], nums[0]
        curmin, curmax = 0, 0
        total = 0

        for n in nums:
            curmax = max(curmax + n, n)
            curmin = min(curmin + n, n)
            total += n
            globalmax = max(globalmax, curmax)
            globalmin = min(globalmin, curmin)
        
        if globalmax < 0:
            return globalmax
        
        return max(globalmax, total - globalmin)