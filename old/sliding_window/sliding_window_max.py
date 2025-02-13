from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0
        while r < len(nums):
            # check if previous number is smaller, then pop it
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # insert the index in queue
            q.append(r)

            # check if left most val in queue is out of sliding wind bounds
            if l > q[0]:
                q.popleft()
            
            # if inside sliding wind, append max value and incr l
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l = l + 1
            r = r + 1
        return res
    
print(Solution().maxSlidingWindow([7,2,4], 2))