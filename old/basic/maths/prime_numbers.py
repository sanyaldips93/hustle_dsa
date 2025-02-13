import math


class Solution:
  def primeNumber(self, num):
    res = []
    i = 1
    m = int(math.sqrt(num))
    while i <= m:
      if num % i == 0:
        res.append(i)
      i += 1
    return len(res) == 1
  
print(Solution().primeNumber(53))