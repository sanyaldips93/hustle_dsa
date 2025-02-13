class Solution:
  def lcm(self, num1, num2):
    greater = num1
    if num1 < num2:
      greater = num2

    while True:
      if (greater % num1 == 0) and (greater % num2 == 0):
        return greater
      greater += 1
  
print(Solution().lcm(24, 52))