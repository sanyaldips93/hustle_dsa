from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda t:t[0])
        newInterval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res
    
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))