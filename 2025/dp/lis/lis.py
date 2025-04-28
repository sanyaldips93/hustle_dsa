from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n)]

        def dfs(i, j):
            if i == n: return 0
            if dp[i][j+1] != -1: return dp[i][j+1]
            nottake = dfs(i+1,j)
            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + dfs(i+1,i)
            dp[i][j+1] = max(take, nottake)
            return dp[i][j+1]
        return dfs(0,-1)
    
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(i-1,-2,-1):
                nt = dp[i+1][j+1]
                t = 0
                if j==-1 or nums[i]>nums[j]:
                    t = 1 + dp[i+1][i+1]
                dp[i][j+1] = max(nt,t)
        
        return dp[0][-1+1]

class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)

        for i in range(n-1,-1,-1):
            dp2 = [0] * (n+1)
            for j in range(i-1,-2,-1):
                nt = dp[j+1]
                t = 0
                if j==-1 or nums[i]>nums[j]:
                    t = 1 + dp[i+1]
                dp2[j+1] = max(nt,t)
            dp = dp2
        
        return dp[-1+1]
    
class Solution4:
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1] * n
        for i in range(n):
            for prev in range(i):
                if arr[prev] < arr[i]:
                    dp[i] = max(dp[i], 1+dp[prev])
        return max(dp[i] for i in range(n))