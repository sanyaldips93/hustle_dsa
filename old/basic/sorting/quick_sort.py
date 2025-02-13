class Solution:
  def quick_sort(self, nums):
    self.qs(nums, 0, len(nums)-1)
    return nums
    

  def qs(self, nums, low, high):
    if low < high:
      j = self.partition(nums, low, high)
      self.qs(nums, 0, j-1)
      self.qs(nums, j+1, high)
  
  def partition(self, nums, low, high):
    pivot = nums[low]
    i, j = low+1, high
    while True:
      while i <= j and nums[i] <= pivot:
          i += 1
      while i <= j and nums[j] >= pivot:
          j -= 1
      if i <= j:
          nums[i], nums[j] = nums[j], nums[i]
      else:
          break
    
    nums[low], nums[j] = nums[j], nums[low]
    return j

print(Solution().quick_sort([3,4,2,5,1]))
    
    