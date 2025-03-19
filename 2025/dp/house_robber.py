from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dfs(n):
            if n < 0:
                return 0
            if n == 0:
                return nums[0]
            if dp[n] != -1:
                return dp[n]
            pick = nums[n] + dfs(n-2)
            nonpick = dfs(n-1)
            dp[n] = max(pick, nonpick)
            return dp[n]
        return dfs(n-1)

class Solution2:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            pick = nums[i] + (dp[i-2] if i-2 >= 0 else 0)
            np = dp[i-1] if i-1 >= 0 else 0
            dp[i] = max(pick, np)
        
        return dp[n-1]

class Solution3:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1]
        for i in range(len(nums)):
            temp = max(nums[i]+rob2, rob1)
            rob1 = rob2
            rob2 = temp
        return rob2

print(Solution2().rob([1,2]))