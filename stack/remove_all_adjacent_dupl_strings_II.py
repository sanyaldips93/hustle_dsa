class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][1] == k:
                stack.pop()
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
        
        if stack and stack[-1][1] == k:
            stack.pop()
        
        res = ""
        for ch, cnt in stack:
            res = res + (ch * cnt)
        return res
        
print(Solution().removeDuplicates("deeedbbcccbdaa", 3))