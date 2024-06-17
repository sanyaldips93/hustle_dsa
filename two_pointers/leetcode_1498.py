# 1498. Number of Subsequences That Satisfy the Given Sum Condition

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        r = len(nums) - 1
        mod = 10 ** 9 + 7
        for i, ele in enumerate(nums):
            while (nums[r] + ele) > target and i <= r:
                r -= 1
            if i <= r:
                res += (1 << (r - i))
                res %= mod
        return res