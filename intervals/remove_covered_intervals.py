from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda t:(t[0], -t[1]))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][0] <= intervals[i][0] and res[-1][1] >= intervals[i][1]:
                continue
            res.append(intervals[i])
        return len(res)
    
print(Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))