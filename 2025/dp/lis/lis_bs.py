from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                ind = self.binarysearch(temp, nums[i])
                temp[ind] = nums[i]
        return len(temp)

    def binarysearch(self, temp, val):
        l, r = 0, len(temp)
        while l <= r:
            m = (l+r) // 2
            if val > temp[m]:
                l = m + 1
            elif val < temp[m]:
                r = m - 1
            else:
                return m
        return l
