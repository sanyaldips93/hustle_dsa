from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return 
            else:
                l = start 
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        kSum(k, 0, target)
        return res
print(Solution().fourSum)