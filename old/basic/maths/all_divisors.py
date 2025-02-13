import math


class Solution:
  def all_divisors(self, num):
    m =  int(math.sqrt(num))
    i = 1
    res = []
    while i <=m :
      if num % i == 0:
        res.append(i)
        if i != num // i:
          res.append(num // i)
      i += 1
    return res
  
print(Solution().all_divisors(36))