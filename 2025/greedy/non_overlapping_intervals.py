from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = intervals
        arr.sort(key=lambda x:x[1])
        prev = arr[0][1]
        cnt = 1
        n = len(arr)

        for ele in arr[1:]:
            if ele[0] >= prev:
                cnt += 1
                prev = ele[1]
        
        return n - cnt