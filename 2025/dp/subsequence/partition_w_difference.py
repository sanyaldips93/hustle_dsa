# Memoization
class Solution:
    def countPartitions(self, arr, d):
        MOD = 10 ** 9 + 7
        n = len(arr)
        total = sum(arr)
        if total - d < 0:
            return 0
        if (total-d) % 2 == 1:
            return 0
        target = (total-d)/2
        dp = {}
        def dfs(i, cur):
            if i == 0:
                if cur == 0 and arr[i] == 0: return 2
                elif cur == 0 or cur == arr[i]: return 1
                else: return 0
            if (i,cur) in dp:
                return dp[(i,cur)]
            npick = dfs(i-1,cur)
            pick = 0
            if arr[i] <= cur:
                pick = dfs(i-1,cur-arr[i])
            dp[(i,cur)] = (pick + npick) % MOD
            return dp[(i,cur)]
        
        return dfs(n-1,target)