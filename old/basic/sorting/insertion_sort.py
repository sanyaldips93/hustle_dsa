class Solution:
  def insertion_sort(self, nums):
    for i in range(1, len(nums)):
      j = i
      while j-1 >= 0:
        if nums[j] < nums[j-1]:
          nums[j], nums[j-1] = nums[j-1], nums[j]
        j -= 1
    return nums

print(Solution().insertion_sort([9989, 4,5,-3,1,2]))