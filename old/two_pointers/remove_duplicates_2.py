from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        counter = 1
        for r in range(l, len(nums)):
            if nums[r] != nums[r-1]:
                counter = 1
                nums[l] = nums[r]
                l += 1
            elif nums[r] == nums[r-1] and counter < 2:
                counter += 1
                nums[l] = nums[r]
                l += 1
        return l, nums
    
print(Solution().removeDuplicates([1,1,1,2,2,3]))