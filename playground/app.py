from collections import defaultdict, deque
from typing import List

# Play with your code
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            length = 0
            if not num-1 in nums:
                length += 1
                while (num + 1) in nums:
                    length += 1
                    num += 1
            res = max(res, length)
        return res 
    
print(Solution().longestConsecutive([1,0,1,2]))