from typing import List

# Memoization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if target % 2:
            return False
        n = len(nums)
        dp = [[-1]*(target+1) for _ in range(n)]
        def dfs(i, cur):
            if cur == 0: return True
            if i == 0: return nums[i] == 0
            if dp[i][cur] != -1:
                return dp[i][cur]
            np = dfs(i-1, cur)
            p = dfs(i-1, cur-nums[i])
            dp[i][cur] = np or p
            return dp[i][cur]
        return dfs(n-1, target)

print(Solution().canPartition([1,5,11,5]))

# Tabulation
class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        if sum(arr) % 2:
            return False
        target = sum(arr) // 2
        n = len(arr)
        dp = [[False]*(target+1) for _ in range(n)]
        for r in range(n):
            dp[r][0] = True
        if arr[0] <= target:
            dp[0][arr[0]] = True
        for r in range(1,n):
            for c in range(target+1):
                pick = False
                if arr[r] <= c:
                    pick = dp[r-1][c-arr[r]]
                dp[r][c] = dp[r-1][c] or pick
        
        return dp[n-1][target]

# Space Optimisation
class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        if sum(arr) % 2:
            return False
        target = sum(arr) // 2
        n = len(arr)
        dp = [False]*(target+1)
        dp[0] = True
        if arr[0] <= target:
            dp[arr[0]] = True
        for r in range(1,n):
            temp = [False]*(target+1)
            temp[0] = True
            for tar in range(target+1):
                pick = False
                if arr[r] <= tar:
                    pick = dp[tar-arr[r]]
                temp[tar] = dp[tar] or pick
            dp = temp
        
        return dp[target]