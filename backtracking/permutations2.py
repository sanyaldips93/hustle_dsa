from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        count = Counter(nums)
        def dfs():
            if len(perm) == len(nums):
                return res.append(perm.copy())
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()
        dfs()
        return res
    
print(Solution().permuteUnique([1,1,2]))