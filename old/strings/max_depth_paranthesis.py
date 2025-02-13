class Solution:
    def maxDepth(self, s: str) -> int:
        open, close, total, res = 0, 0, 0, 0
        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                open -= 1
            if open > 0:
                res = max(res, open)
        return res

print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))