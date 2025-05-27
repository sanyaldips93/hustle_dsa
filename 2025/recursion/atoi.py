class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign, idx = 1, 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if s[0] == '-':
            sign = -1
            idx += 1
        elif s[0] == '+':
            idx += 1
        
        
        def helper(idx, res):
            if idx >= len(s) or not s[idx].isdigit():
                return res
            
            dig = int(s[idx])
            
            if res > (INT_MAX - dig) // 10:
                return (INT_MAX) if sign == 1 else -INT_MIN

            return helper(idx+1, res * 10 + dig)
        
        res = helper(idx, 0)
        return sign * res