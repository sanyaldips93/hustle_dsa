class Solution:
  def sum_num(self, n):
    count = 0
    def recurse(n):
      nonlocal count
      if n == 0:
        return count
      count += n
      return recurse(n-1)
    return recurse(n)
  

class Solution1:
  def sum_num(self, n):
    if n == 0:
      return 0
    return n + self.sum_num(n-1)
  
print(Solution1().sum_num(10))