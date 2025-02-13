class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, open = [], 0
        for ch in s:
            if ch == '(' and open > 0: res.append(ch)
            elif ch == ')' and open > 1: res.append(ch)
            open += 1 if ch == '(' else -1
        return "".join(res)

print(Solution().removeOuterParentheses("((()()))(())"))