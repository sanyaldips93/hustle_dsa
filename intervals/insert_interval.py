from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # Case 1 - The current interval is non overlapping and comes after newInterval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            # Case 2 - The current interval is non overlapping and comes before newInterval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Case 3 - Overlapping condition
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)
        return res

print(Solution().insert([[1,3],[6,9]], [2,5]))