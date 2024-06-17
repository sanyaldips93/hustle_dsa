class Solution:
  def print_num(self, n):
      if n == 0:
        return
      print(n)
      self.print_num(n-1)
  
print(Solution().print_num(4))