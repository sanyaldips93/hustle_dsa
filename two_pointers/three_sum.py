from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev = None
        for i in range(len(nums) - 1):
            if nums[i] == prev:
                continue;
            l, r = i + 1, len(nums) - 1
            while l < r:
                one, two, three = nums[i], nums[l], nums[r]
                if(one + two + three > 0):
                    r = r - 1
                elif(one + two + three < 0):
                    l = l + 1
                else:
                    res.append([one, two, three])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            prev = nums[i]
        return res

'''
while nums[l] == nums[l-1] and l < r:
  l += 1
This bit is imporant - as we are just forwarding the left pointer to rule out duplicacy.
'''