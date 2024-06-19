class Solution:
  def mergeSort(self, nums):
    if len(nums) <= 1:
          return nums 
    mid = len(nums) // 2
    left = self.mergeSort(nums[:mid])
    right = self.mergeSort(nums[mid:])
    return self.merge(left, right)

  def merge(self, left, right):
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
      if left[l] < right[r]:
        res.append(left[l])
        l += 1
      else:
        res.append(right[r])
        r += 1
    
    while l < len(left):
      res.append(left[l])
      l += 1
    
    while r < len(right):
      res.append(right[r])
      r += 1

    return res
  
print(Solution().mergeSort([6,4,5,3,1,7,2]))