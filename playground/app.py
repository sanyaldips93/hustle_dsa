from collections import defaultdict, deque
from typing import List

# Play with your code
from typing import List
from collections import deque
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1] * (target+1) for _ in range(n)]

        def dfs(i, cur):
            if i == -1:
                if cur == target: return 1
                else: return 0
            if dp[i][cur] != -1:
                return dp[i][cur]
            
            np = dfs(i-1,cur+nums[i])
            p = dfs(i-1,cur-nums[i])
            dp[i][cur] = p + np
            return dp[i][cur]
        
        return dfs(n-1,0)

print(Solution().findTargetSumWays([1,1],1))