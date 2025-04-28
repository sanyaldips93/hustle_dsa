class Solution:
  def palindromePartitioning(s: str) -> int:
      n = len(s)
      dp = [-1] * n

      def isPalindrome(i,j):
          while i < j:
              if s[i] != s[j]: return False
              i += 1
              j -= 1
          return True

      def dfs(i):
          if i == n: return 0
          if dp[i] != -1: return dp[i]
          mincost = n
          for j in range(i, n):
              if isPalindrome(i,j):
                  cost = 1+ dfs(j+1)
                  mincost = min(mincost, cost)
          dp[i] = mincost
          return mincost
      
      return dfs(0) - 1


  def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)

        def isPalindrome(i,j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        
        for i in range(n-1, -1, -1):
            mincost = n
            for j in range(i, n):
                if isPalindrome(i,j):
                    cost = 1+ dp[j+1]
                    mincost = min(mincost, cost)
            dp[i] = mincost
        return dp[0] - 1