class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l, r = l+1, r-1
        return True
    
'''
Example - 'abbca'
There is a conflict at index 1 and 3.. so we check the substring bbc without c and without b at a time, and see
if either of them is palindrome or not. if it is we return true or we return false
'''