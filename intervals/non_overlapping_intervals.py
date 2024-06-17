from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda t:t[0])
        newInterval = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            # Case 1 - Non overlapping
            if newInterval[1] <= intervals[i][0]:
                newInterval = intervals[i]
            # Case 2 - Overlapping
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), min(intervals[i][1], newInterval[1])]
                res += 1
        return res

print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))