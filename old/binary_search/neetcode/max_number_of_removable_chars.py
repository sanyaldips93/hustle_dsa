from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def issub(s1, s2):
            i1, i2 = 0, 0
            while i1 < len(s1) and i2 < len(s2):
                if i1 in removed or s1[i1] != s2[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            return i2 == len(s2)
        
        l, r = 0, len(removable) - 1
        res = 0
        while l <= r:
            m = l + ((r - l) // 2)
            removed = set(removable[:m+1])
            if issub(s, p):
                l = m + 1
                res = max(res, m + 1)
            else:
                r = m - 1
        
        return res


            