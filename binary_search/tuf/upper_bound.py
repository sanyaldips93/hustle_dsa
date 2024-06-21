class Solution:
  def upper_bound(self, arr, num):
    l, r = 0, len(arr) - 1
    ans = 0
    while l <= r:
      m = (l + r) // 2
      if arr[m] > num:
        ans = m
        r = m - 1
      else:
        l = m + 1
    return ans

print(Solution().upper_bound([2,4,5,9,11], 4))