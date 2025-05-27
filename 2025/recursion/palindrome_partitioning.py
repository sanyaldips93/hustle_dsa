from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(i, j, s):
                    cur.append(s[i:j+1])
                    dfs(j+1, cur)
                    cur.pop()
        
        dfs(0, [])
        return res

    def isPali(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True