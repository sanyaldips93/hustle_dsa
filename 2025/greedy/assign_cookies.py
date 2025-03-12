from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l, res = 0, 0
        for child in g:
            while l < len(s):
                if s[l] >= child:
                    res += 1
                    l += 1
                    break
                l += 1
        return res