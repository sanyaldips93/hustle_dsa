from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        start = money
        cnt = 0
        for price in prices:
            if start-price >= 0:
                start -= price
                cnt += 1
            if cnt == 2:
                break
        return start if cnt == 2 else money
    
print(Solution().buyChoco([1,2,2], 3))