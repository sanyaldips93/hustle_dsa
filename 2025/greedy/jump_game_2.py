from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, jumps):
            if i >= n-1: return jumps
            if (i, jumps) in dp: return dp[(i, jumps)]
            mini = float("inf")
            for j in range(1, nums[i]+1):
                mini = min(mini, dfs(i+j, jumps+1))
            dp[(i, jumps)] = mini
            return mini
        return dfs(0,0)

print(Solution().jump([2,3,1,1,4]))

class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0         # l and r define the current range of indices we can jump from
        jumps = 0         # Count of jumps made

        # We stop once we've reached or passed the last index
        while r < n - 1:
            farthest = 0

            # Explore all positions in the current range [l, r]
            for i in range(l, r + 1):
                # From each position i, see how far we can jump
                farthest = max(farthest, i + nums[i])

            # Move to the next range of indices [r+1, farthest]
            l = r + 1
            r = farthest

            # We made one jump to get to this new range
            jumps += 1

        return jumps