class Solution:
  def fibonacci(self, n):
    if n == 0:
      return [0]
    if n == 1:
      return [0, 1]
    res = [0, 1]
    def build(j):
      if j <= n:
        res.append(res[-1] + res[-2])
        build(j+1)
    build(2)
    return res

print(Solution().fibonacci(5))