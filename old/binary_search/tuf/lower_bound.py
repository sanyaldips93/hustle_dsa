class Solution:
  def lower_bound(self, arr, num):
    l, r = 0, len(arr) - 1
    ans = 0
    while l <= r:
      m = (l + r) // 2
      if arr[m] <= num:
        ans = m
        l = m + 1
      else:
        r = m - 1
    return ans

print(Solution().lower_bound([2,4,5,8,9,11], 5))