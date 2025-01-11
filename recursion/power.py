class Solution:
    def myPow(self, x: float, n: int) -> float:
        def getPow(y, m):
            if m == 0: return 1
            if y == 0: return 0

            res = getPow(y, m // 2)
            return res * res if m % 2 == 0 else res * res * y
            
        
        res = getPow(x, abs(n))
        return res if n > 0 else 1/res
    
print(Solution().myPow(2.00000, -10)) # 1024.00000