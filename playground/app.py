from collections import defaultdict, deque
from typing import List

# Play with your code
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = 0
        res = 0
        for child in g:
            while l < len(s) and  s[l] < child:
                l += 1
            if l >= len(s):
                return res
            res += 1
            l += 1
        return res
    
print(Solution().findContentChildren([1,2,3], [1,1]))