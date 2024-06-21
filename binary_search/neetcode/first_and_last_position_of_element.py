from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]
    
    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                idx = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return idx