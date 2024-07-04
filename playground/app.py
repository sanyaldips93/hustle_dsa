from collections import defaultdict
from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base cases
        if n == 0:
            return 1
        if n == 1:
            return x

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        # Recursive calculation
        # If n is even
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        # If n is odd
        else:
            half = self.myPow(x, (n - 1) // 2)
            return x * half * half

print(Solution().myPow(2.0, -2))