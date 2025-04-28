from typing import List


class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp, cnt = [1] * n, [1] * n
        maxi = 0
        for i in range(n):
            for prev in range(i):
                if arr[prev] < arr[i] and 1+dp[prev] > dp[i]:
                    dp[i] = 1+dp[prev]
                    cnt[i] = cnt[prev]
                elif arr[prev] < arr[i] and 1+dp[prev] == dp[i]:
                    cnt[i] += cnt[prev]
            maxi = max(maxi, dp[i])
        

        res = 0
        for i in range(n):
            if dp[i] == maxi: res += cnt[i]
        
        return res