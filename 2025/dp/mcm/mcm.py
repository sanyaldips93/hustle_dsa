def matrixMultiplication(arr, n):
	dp = [[float("inf")] * n for _ in range(n)]
	for i in range(n):
		dp[i][i] = 0
	for i in range(n-1, 0, -1):
		for j in range(i+1, n):
			for k in range(i,j):
				dp[i][j] = min(dp[i][j], arr[i-1]*arr[k]*arr[j]+dp[i][k]+dp[k+1][j])
	return dp[1][n-1]


def matrixMultiplication(arr, n):
	dp = [[float("inf")] * n for _ in range(n)]
	def dfs(i, j):
		if i == j: return 0
		if dp[i][j] != float("inf"): return dp[i][j]
		for k in range(i,j):
			dp[i][j] = min(dp[i][j], arr[i-1]*arr[j]*arr[k] + dfs(i,k) + dfs(k+1,j))
		return dp[i][j]
	return dfs(1,n-1)