from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for n in pushed:
            stack.append(n)
            while stack and i < len(popped) and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return stack == []