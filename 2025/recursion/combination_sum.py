from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recursion(i, cur, total):
            if i >= len(candidates) or total < 0:
                return
            if total == 0:
                res.append(cur.copy())
                return
            
            cur.append(candidates[i])
            recursion(i, cur, total-candidates[i])
            cur.pop()
            recursion(i+1, cur, total)
        
        recursion(0, [], target)
        return res