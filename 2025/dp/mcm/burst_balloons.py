from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        # Add 1 to the beginning and end to handle edge balloons (avoids out-of-bounds)
        nums = [1] + nums + [1]

        # Create a DP table where dp[i][j] stores the max coins we can get
        # from bursting all balloons between index i and j (1-based in original list)
        dp = [[-1] * (n + 2) for _ in range(n + 2)]

        # Recursive function to compute max coins from index i to j
        def dfs(i, j):
            # Base case: if i > j, no balloons to burst
            if i > j:
                return 0

            # If already computed, return the stored value
            if dp[i][j] != -1:
                return dp[i][j]

            # Try bursting each balloon `k` in range [i, j] as the last one in this subarray
            for k in range(i, j + 1):
                # coins = coins from bursting k last in this segment
                # = nums[i-1]*nums[k]*nums[j+1] (as if k is surrounded by i-1 and j+1)
                # + coins from left side (i to k-1) + coins from right side (k+1 to j)
                coins = nums[i - 1] * nums[k] * nums[j + 1] + dfs(i, k - 1) + dfs(k + 1, j)

                # Update dp[i][j] with the max coins possible
                dp[i][j] = max(dp[i][j], coins)

            return dp[i][j]

        # Start the recursion from the full original array (excluding the added 1s)
        return dfs(1, n)

# Tabulation
class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n+2) for _ in range(n+2)]
        
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j: continue
                for k in range(i,j+1):
                    dp[i][j] = max(dp[i][j], nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j])
        
        return dp[1][n]