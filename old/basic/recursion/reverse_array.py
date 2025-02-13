
class Solution:
  def rev_arr(self, arr):
    def reverse(arr, s, e):
      if s <= e:
        arr[s], arr[e] = arr[e], arr[s]
        return reverse(arr, s+1, e-1)
    reverse(arr, 0, len(arr) - 1)
    return arr
      
print(Solution().rev_arr([1,2,3,4,5]))