from collections import defaultdict
from typing import List

class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, tmp):
            if sum(tmp) == target:
                return res.append(tmp.copy())
            if i >= len(arr) or sum(tmp) > target:
                return
            tmp.append(arr[i])
            dfs(i+1, tmp)
            tmp.pop()
            dfs(i+1, tmp)
        dfs(0, [])
        return len(res)
        

print(Solution().combinationSum([2,3,6,7], 7))