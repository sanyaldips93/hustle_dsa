from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            val = arr[m] -( m + 1)
            if val < k:
                l = m + 1
            else:
                r = m - 1
        return l + k
    
print(Solution().findKthPositive([2,3,4,9], 2))