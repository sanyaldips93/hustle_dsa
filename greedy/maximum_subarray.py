from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = nums[0]
        cursum = 0
        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxs = max(maxs, cursum)
        return maxs