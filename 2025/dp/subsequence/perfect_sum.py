
# Memoization without handling [0] subset case
class Solution:
	def perfectSum(self, arr, target):
		n = len(arr)
		dp = {}
		def dfs(i, cur):
			if i == 0:
				if cur == 0 and arr[i] == 0:
					return 2
				elif cur == 0 or cur == arr[i]:
					return 1
				else: return 0
			if (i,cur) in dp:
				return dp[(i,cur)]
			npick = dfs(i-1, cur)
			pick = 0
			if arr[i] <= cur:
				pick = dfs(i-1, cur-arr[i])
			dp[(i,cur)] = pick+npick
			return dp[(i,cur)]
		return dfs(n-1,target)
      
print(Solution().perfectSum([2,5,1,4,3],10))

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
