class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                stack.append(int(multiplier) * temp)
        return "".join(stack)