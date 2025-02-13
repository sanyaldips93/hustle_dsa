class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        if len(s) == 0:
            return res
        i, sign = 0, 1
        while i < len(s):
            if s[i] == ' ':
                i += 1
            else: break
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            sign = 1
            i += 1
        while i < len(s):
            if ord(s[i]) < 48 or ord(s[i]) > 57:
                break
            res = res * 10 + int(s[i])
            i += 1
        
        res = res * sign
        if res > (2**31 - 1):
            return 2**31 - 1
        elif res < (-2**31):
            return -2**31
        else:
            return res

print(Solution().myAtoi("    -042"))