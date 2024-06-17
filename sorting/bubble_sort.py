from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = True
        def bubble(nums):
          swap = False
          for r in range(1, len(nums)):
            l = r - 1
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                swap = True
          return swap
        while res:
           res = bubble(nums)
        return nums
    
print(Solution().sortArray([4,7,1,5]))