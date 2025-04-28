from typing import List


class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        n = len(arr)
        dp = [1] * n
        hash = [i for i in range(n)]
        maxval, li = 0, 0
        arr.sort()
        for i in range(n):
            for prev in range(i):
                if arr[i] % arr[prev] == 0 and 1+dp[prev] > dp[i]:
                    dp[i] = 1+dp[prev]
                    hash[i] = prev
            if dp[i] > maxval:
                maxval = dp[i]
                li = i
        narr = []
        while hash[li] != li:
            narr.append(arr[li])
            li = hash[li]
        narr.append(arr[li])
        return narr[::-1]

print(Solution().largestDivisibleSubset([1,3,7,9,27]))