from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L , R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        return L
    
  

# idea - this problem comes down to the last searchable group. if the target is bigger than that, we will automatically
# decrease R and it will become out of bounds, hence L will be the place for the local shortest value
# However, if target is bigger than that, we will automatically increase L and it will become out of bounds, hence L+1 will be
# the place for the local shortest value, but we will still send L as we would have increased L and made it out of bounds.