class Solution:
  def gcd(self, num1, num2):
    lesser = num1
    if num1 < num2:
      lesser = num2

    while True:
      if (num1 % lesser == 0) and (num2 % lesser == 0):
        return lesser
      lesser -= 1
  
print(Solution().gcd(36, 60))