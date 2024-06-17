class Solution:
  def armstrong(self, num):
    arr = []
    res = 0
    src = num
    while num != 0:
      digit = num % 10
      num = num // 10
      arr.append(digit)
    length = len(arr)
    for n in arr:
      res += n ** length
    return res == src
  
print(Solution().armstrong(153))
