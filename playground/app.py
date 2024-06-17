from collections import defaultdict
from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        temp = x
        x = abs(x)
        while x != 0:
            digit = x % 10
            x = x // 10
            res = res * 10 + digit
        if temp < 0:
            return -res
        else:
            return res

print(Solution().reverse(123))