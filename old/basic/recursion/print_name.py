class Solution:
  def recurse(self, n):
    while n > 0:
      print('Jai Siya Ram')
      return self.recurse(n-1)
  
print(Solution().recurse(4))