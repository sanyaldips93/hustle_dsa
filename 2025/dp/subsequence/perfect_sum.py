
# Memoization
class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = {}  # Memoization dictionary to store (i, cur) -> number of ways
        
        def dfs(i, cur):
            # Base case: if we are at the first element (i==0)
            if i == 0:
                # If target is 0 and arr[0] is 0, two choices: pick or not pick the zero
                if cur == 0 and arr[i] == 0:
                    return 2
                # If target is 0 or target matches arr[0], exactly 1 way (either pick it or ignore)
                elif cur == 0 or cur == arr[i]:
                    return 1
                # Otherwise, no valid way
                else:
                    return 0
            
            # If already solved this subproblem, return cached answer
            if (i, cur) in dp:
                return dp[(i, cur)]

            # Two choices at each step: 
            # 1. Do not pick the current element
            npick = dfs(i-1, cur)

            # 2. Pick the current element (only if arr[i] <= cur)
            pick = 0
            if arr[i] <= cur:
                pick = dfs(i-1, cur-arr[i])

            # Total ways = pick ways + non-pick ways
            dp[(i, cur)] = pick + npick
            return dp[(i, cur)]
        
        # Start the recursion from last index with full target
        return dfs(n-1, target)

# Example usage
print(Solution().perfectSum([2,5,1,4,3], 10))


# Tabulation
class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n)]

        # Base case: filling for index 0
        if arr[0] == 0:
            dp[0][0] = 2  # pick or not pick
        else:
            dp[0][0] = 1  # only not pick (empty subset)
            if arr[0] <= target:
                dp[0][arr[0]] = 1  # only pick

        for i in range(1, n):
            for t in range(target + 1):
                npick = dp[i - 1][t]
                pick = 0
                if arr[i] <= t:
                    pick = dp[i - 1][t - arr[i]]
                dp[i][t] = pick + npick

        return dp[n - 1][target]


# Space Optimisation
