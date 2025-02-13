
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

# Solution 1
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

# Solution 2
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            start, end = i.start, i.end
            time.append((start, 1))
            time.append((end, -1))
        time.sort(key=lambda t:(t[0], t[1])) 
        '''
        [(0, 1), (5, 1), (10, -1), (10, 1), (20, -1), (40, -1)]
        Why (10, -1) before (10, 1) -> because we are considering the blocks to be nonoverlapping, and one room can fit
        both meetings.
        
        Logically we are stacking start and end blocks such that when we loop through consecutive start blocks
        would increase the counter but an end block will decrease the counter representing that the current window
        would require another room for another meeting.

        We are taking the max counts possible to host all the meetings together.
        '''
        count, res = 0, 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res
    
# Test case = [(0,40),(5,10),(10,20)]