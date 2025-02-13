from typing import List


class Solution:
  def wordBreak(self, s, arr: List[str]):
    
    def backtrack(i):
      if i == len(s):
        return True
      
      for j in range(i+1, len(s)+1):
        if s[i:j] in arr and backtrack(j):
          return True
      
      return False
    
    return backtrack(0)

print(Solution().wordBreak("apipeap", ["ap", "ipe"]))