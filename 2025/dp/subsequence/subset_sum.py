# Recursion TC - O(2*n), SC O(n * sum) + O(n)
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        def dfs(n, target):
            if target == 0:
                return True
            if n == 0:
                return arr[0] == target
            npick = dfs(n-1, target)
            pick = False
            if arr[n] <= target:
                pick = dfs(n-1, target-arr[n])
            
            return npick or pick
        return dfs(n-1, sum)

# Memoization TC - O(n*sum), SC O(n * sum) + O(n)
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[-1] * (sum+1) for _ in range(n)]
        def dfs(n, target):
            if target == 0:
                return True
            if n == 0:
                return arr[0] == target
            if dp[n][target] != -1:
                return dp[n][target]
            npick = dfs(n-1, target)
            pick = False
            if arr[n] <= target:
                pick = dfs(n-1, target-arr[n])
            
            dp[n][target] =  npick or pick
            return dp[n][target]
        return dfs(n-1, sum)
    
# Tabulation TC - O(n*sum), SC O(n * sum)
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[False] * (sum+1) for _ in range(n)]
        
        for r in range(0,n):
            dp[r][0] = True
        
        if arr[0] <= sum:
            dp[0][arr[0]] = True
        
        for r in range(1, n):
            for target in range(0, sum+1):
                nottake = dp[r-1][target]
                take = False
                if arr[r] <= target:
                    take = dp[r-1][target-arr[r]]
                dp[r][target] = nottake or take
        
        return dp[n-1][sum]

# Space Optimisation TC - O(n*sum), SC O(sum)
class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [False] * (sum+1)
        dp[0] = True
        
        if arr[0] <= sum:
            dp[arr[0]] = True
        
        for r in range(1, n):
            temp = [False] * (sum+1)
            temp[0] = True
            for target in range(0, sum+1):
                nottake = dp[target]
                take = False
                if arr[r] <= target:
                    take = dp[target-arr[r]]
                temp[target] = nottake or take
            dp = temp
        
        return dp[sum]