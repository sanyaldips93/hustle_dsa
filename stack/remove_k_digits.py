class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for dig in num:
            while stack and stack[-1] > dig and k > 0:
                stack.pop()
                k -= 1
            if stack or dig is not '0':
                stack.append(dig)
        stack = stack[:len(stack) - k]
        res = "".join(stack) or "0"
        return res