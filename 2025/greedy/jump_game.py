from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex = 0
        n = len(nums)
        for i in range(n):
            if i > maxindex: return False
            maxindex = max(maxindex, nums[i]+i)
            if maxindex >= n-1: return True
        return True