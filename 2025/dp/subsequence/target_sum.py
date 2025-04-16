from collections import defaultdict
from typing import List

# Recursion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(n, cur):
            if n == -1: 
                if cur == target:
                    return 1
                return 0
            return (dfs(n-1, cur + nums[n]) + dfs(n-1, cur - nums[n]))
        return dfs(n-1, 0)

# Memoization  
class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(n, cur):
            if (n, cur) in dp:
                return dp[(n, cur)]
            if n == -1: 
                if cur == target:
                    return 1
                return 0
            dp[(n, cur)] = dfs(n-1, cur + nums[n]) + dfs(n-1, cur - nums[n])
            return dp[(n, cur)]
        return dfs(n-1, 0)

# Tabulation  
class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1 # for 0 elements there is only one way(count) to have 0 sum
        for i in range(n):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum + nums[i]] += count
                dp[i+1][cur_sum - nums[i]] += count
        
        return dp[n][target]
    

# Memoization (best)
class Solution4:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        offset = total
        dp = [[-1] * (2*total+1) for _ in range(n)]

        def dfs(i, cur):
            if i == -1:
                return 1 if cur == target else 0

            if dp[i][cur+offset] != -1:
                return dp[i][cur+offset]
            
            plus = dfs(i-1,cur+nums[i])
            minus = dfs(i-1,cur-nums[i])
            dp[i][cur+offset] = plus + minus
            return dp[i][cur+offset]
        
        return dfs(n-1,0)

# Single Array Optimisation
class Solution5:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        n = len(arr)
        total = sum(arr)
        if total - target < 0: return 0
        if (total - target) % 2: return 0
        d = (total - target) // 2

        dp = [0] * (d+1)
        dp[0] = 1
        
        for r in range(n):
            for tar in range(d, arr[r]-1, -1):
                dp[tar] = dp[tar] + dp[tar-arr[r]]
        
        return dp[d]


