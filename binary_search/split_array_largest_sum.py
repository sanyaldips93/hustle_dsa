from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            sub = 0
            cur = 0
            for n in nums:
                cur += n
                if cur > largest:
                    sub += 1
                    cur = n
            return sub + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
    
print(Solution().splitArray([7,2,5,10,8], 2))