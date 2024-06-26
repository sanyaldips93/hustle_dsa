from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        target = m * k
        if len(bloomDay) < target:
            return -1
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            val = self.possible(bloomDay, mid, m, k)
            if val:
                r = mid - 1
            else:
                l = mid + 1
        return l
    def possible(self, arr, mid, m, k):
        cnt = 0
        bou = 0
        for num in arr:
            if num <= mid:
                cnt += 1
            else:
                bou += cnt // k
                cnt = 0
        bou += cnt // k
        return bou >= m
    
print(Solution().minDays([1,10,3,10,2], 3, 1))