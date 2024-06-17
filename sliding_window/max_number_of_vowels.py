class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res, vowels = 0, 0
        arr = ['a', 'e', 'i', 'o', 'u']
        for i in range(k-1):
            if s[i] in arr:
                vowels += 1

        i = 0
        for j in range(k-1, len(s)):
            if s[j] in arr:
                vowels += 1
            res = max(res, vowels)
            if s[i] in arr:
                vowels -= 1
            i += 1
        
        return res
    
print(Solution().maxVowels('tnfazcwrryitgacaabwm', 4))