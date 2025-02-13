class Solution:
  def print_num(self, n):
    i = 1
    def recurse(i):
      if i > n:
        return
      print(i)
      recurse(i+1)
    recurse(i)
  
print(Solution().print_num(4))