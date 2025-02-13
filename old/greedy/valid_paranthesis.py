class Solution:
    def checkValidString(self, s: str) -> bool:
        lmax, lmin = 0, 0
        for ch in s:
            if ch == '(':
                lmax += 1
                lmin += 1
            elif ch == ")":
                lmax -= 1
                lmin -= 1
            else:
                lmax += 1
                lmin -= 1
            if lmax < 0:
                return False
            if lmin < 0:
                lmin = 0
        
        return lmin == 0