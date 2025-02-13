from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t
        thash, shash = defaultdict(int), defaultdict(int)
        for char in t:
            thash[char] += 1
        have, need = 0, len(thash)
        l, res, reslen = 0, [-1, -1], float("inf")
        for r in range(len(s)):
            rchar = s[r]
            shash[rchar] += 1

            if rchar in thash and thash[rchar] == shash[rchar]:
                have += 1

            while have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = [l, r]
                
                shash[s[l]] -= 1
                if s[l] in thash and shash[s[l]] < thash[s[l]]:
                    have -= 1
                l += 1
        [l, r] = res
        return s[l:r + 1] if reslen != float("inf") else ""

print(Solution().minWindow('abc', 'ab'))