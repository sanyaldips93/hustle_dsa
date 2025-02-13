from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        def backtrack(i, dots, cur):
            if dots == 4 and i == len(s):
                return res.append(cur[:-1])
            if dots > 4:
                return

            for j in range(i, len(s)):
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != '0'):
                    backtrack(j+1, dots + 1, cur + s[i:j+1] + ".")
        
        backtrack(0, 0, "")
        return res

print(Solution().restoreIpAddresses("101023"))