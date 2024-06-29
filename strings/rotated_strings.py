class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            lastchar = s[-1]
            tmp = lastchar + s[:-1]
            if tmp == goal:
                return True
            s = tmp
        return False

print(Solution().rotateString('abcde', 'cdeab'))