from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def recursion(i, cur, total):
            if total == 0:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total < 0:
                return
            cur.append(candidates[i])
            recursion(i+1, cur, total-candidates[i])
            cur.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i = i+1
            recursion(i+1, cur, total)
        
        recursion(0, [], target)
        return res
    
print(Solution().combinationSum2([2,5,2,1], 5))