from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = intervals
        arr.sort(key=lambda x:x[0])
        n = len(arr)
        prev = arr[0]
        res = []
        for i in range(1,n):
            if prev[1] >= arr[i][0]:
                prev[1] = max(arr[i][1], prev[1])
            else:
                res.append(prev)
                prev = arr[i]
        res.append(prev)
        return res