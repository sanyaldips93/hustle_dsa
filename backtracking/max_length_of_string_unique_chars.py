from collections import Counter
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charset = set()
        def overlap(s, charset):
            charmap = Counter(s) + Counter(charset)
            return max(charmap.values()) > 1
        
        def dfs(i, charset):
            if i == len(arr):
                return len(charset)
            res = 0
            if not overlap(arr[i], charset):
                for c in arr[i]:
                    charset.add(c)
                res = dfs(i+1, charset)
                for c in arr[i]:
                    charset.remove(c)
                
            return max(res, dfs(i+1, charset))
        
        return dfs(0, charset)
    
print(Solution().maxLength(["ab", "cd", "ef"]))