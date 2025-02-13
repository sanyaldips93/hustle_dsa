from collections import defaultdict
from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash1 = defaultdict(List)
        hash2 = defaultdict(List)
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if s[i] not in hash1:
                hash1[s[i]] = pattern[i]
            if pattern[i] not in hash2:
                hash2[pattern[i]] = s[i]
        for i in range(len(s)):
            if hash1[s[i]] != pattern[i] or hash2[pattern[i]] != s[i]:
                return False
        return True
  
print(Solution().wordPattern('abba', 'dog, cat, cat, fish'))