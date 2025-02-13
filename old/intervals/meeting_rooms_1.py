class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda t:t.start)
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < end:
                return False
            start = intervals[i].start
            end = intervals[i].end
        return True