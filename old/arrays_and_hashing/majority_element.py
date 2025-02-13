from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxL = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxL else res
            maxL = max(maxL, count[n])
        return res
    
    # Boyer - Moore's algorithm
    def majorityElement2(self, nums: List[int]) -> int:
        res, count = 0,0
        for i in nums:
            if count == 0:
                res = i
            
            if i != res:
                count -= 1
            else: count += 1
        return res