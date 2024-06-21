class Solution:
  def floor_ceil_val(self, arr, x):
    l, r = 0, len(arr) - 1
    floor, ceil = -1, -1
    while l <= r:
      m = (l + r) // 2
      if arr[m] < x:
        floor = arr[m]
        l = m + 1
      else:
        ceil = arr[m]
        r = m - 1
    return [floor, ceil]
  
print(Solution().floor_ceil_val([3,4,4,7,8,10], 10))