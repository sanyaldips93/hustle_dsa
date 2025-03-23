from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[:-1]
        nums2 = nums[1:]

        def innerRob(nums):
            n = len(nums)
            dp = [-1] * n
            dp[0] = nums[0]
            for i in range(1, n):
                pick = nums[i] + (dp[i-2] if i-2 >= 0 else 0)
                np = dp[i-1]
                dp[i] = max(pick, np)
            return dp[n-1]
        
        return max(innerRob(nums1), innerRob(nums2))