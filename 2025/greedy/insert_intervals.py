from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        arr = intervals
        nwint = newInterval
        n = len(arr)
        while i < n and arr[i][1] < nwint[0]:
            res.append(arr[i])
            i += 1
        while i < n and arr[i][0] <= nwint[1]:
            nwint[0] = min(arr[i][0], nwint[0])
            nwint[1] = max(arr[i][1], nwint[1])
            i += 1
        res.append(nwint)
        while i < n:
            res.append(arr[i])
            i += 1
        return res

print(Solution().insert([[1,3],[6,9]], [2,5]))