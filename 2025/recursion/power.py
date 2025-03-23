class Solution:
    def myPow(self, x: float, n: int) -> float:
        def backtrack(x, y):
            if x == 0:
                return 0
            if y == 0:
                return 1
            
            res = backtrack(x, y // 2)
            return res * res if y % 2 == 0 else res * res * x
        
        res = backtrack(x, abs(n))
        return res if n >= 0 else 1/res

print(Solution().myPow(2.00, -2))