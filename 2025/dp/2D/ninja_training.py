
# Memoization
class Solution:
    def maximumPoints(self, arr):
        # Code here
        n = len(arr)
        dp = [[-1] * 3 for _ in range(n)]
        def backtrack(idx, last):
            if dp[idx][last] != -1:
                return dp[idx][last]
            
            if idx == -1:
                return 0
            
            maxe = 0
            for i in range(len(arr[0])):
                if i != last:
                    points = arr[idx][i] + backtrack(idx-1, i)
                    maxe = max(maxe, points)
            dp[idx][last] = maxe
            return dp[idx][last]

        res = backtrack(n-1, -1)
        print(dp)
        return res
print(Solution().maximumPoints( [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))

# Memoization 2
class Solution2:
    def maximumPoints(self, arr):
        # Code here
        n = len(arr)
        m = len(arr[0])
        
        dp = [[-1] * (m+1) for _ in range(n)]
        
        def dfs(idx, last):
            if dp[idx][last] != -1:
                return dp[idx][last]
            
            if idx == 0:
                for j in range(m):
                    if last != j:
                        dp[idx][last] = max(dp[idx][last], arr[idx][j])
                return dp[idx][last]

            for j in range(m):
                if last != j:
                    dp[idx][last] = max(dp[idx][last], arr[idx][j]+dfs(idx-1, j))
                    
            return dp[idx][last]
        
        return dfs(n-1, m)

# Tabulation
class Solution3:
    def maximumPoints(self, arr):
        # Code here
        n = len(arr)
        m = len(arr[0])
        
        dp = [[-1] * (m+1) for _ in range(n)]
        
        dp[0][0] = max(arr[0][1], arr[0][2])
        dp[0][1] = max(arr[0][0], arr[0][2])
        dp[0][2] = max(arr[0][0], arr[0][1])
        dp[0][3] = max([arr[0][0], arr[0][1], arr[0][2]])
        
        for i in range(1,n):
            for k in range(m+1):
                dp[i][k] = 0
                maxval = 0
                for j in range(m):
                    if j != k:
                        maxval = max(maxval, arr[i][j] + dp[i-1][j])
                dp[i][k] = maxval
        
        return dp[n-1][m]

# Space Optimisation
class Solution4:
    def maximumPoints(self, arr):
        # Code here
        n = len(arr)
        m = len(arr[0])
        
        dp = [-1] * 4
        
        dp[0] = max(arr[0][1], arr[0][2])
        dp[1] = max(arr[0][0], arr[0][2])
        dp[2] = max(arr[0][0], arr[0][1])
        dp[3] = max([arr[0][0], arr[0][1], arr[0][2]])
        
        for i in range(1,n):
            temp = [-1] * 4
            for k in range(m+1):
                for j in range(m):
                    if j != k:
                        temp[k] = max(temp[k], arr[i][j] + dp[j])
            dp = temp
        
        return dp[m]