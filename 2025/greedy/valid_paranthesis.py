class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(i, open):
            if open < 0: return False
            if i == n: return open == 0
            if s[i] == '(': return dfs(i+1, open+1)
            elif s[i] == ')': return dfs(i+1, open-1)
            else:
                return dfs(i+1, open+1) or dfs(i+1, open-1) or dfs(i+1, open)
        n = len(s)
        return dfs(0, 0)
    
print(Solution().checkValidString("()"))