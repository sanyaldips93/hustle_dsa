from typing import List


class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1] * n
        hash = [i for i in range(n)]
        maxval, li = 0, -1
        for i in range(n):
            for prev in range(i):
                if arr[prev] < arr[i]:
                    dp[i] = max(dp[i], 1+dp[prev])
                    hash[i] = prev
            if dp[i] > maxval:
                maxval = dp[i]
                li = i
        narr = []
        while hash[li] != li:
            narr.append(arr[li])
            li = hash[li]
        narr.append(arr[li])
        print(narr[::-1])
        return maxval