from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res