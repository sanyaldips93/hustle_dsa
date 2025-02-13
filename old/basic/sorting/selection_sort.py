class Solution:
  def selection_sort(self, nums):
    for i in range(len(nums)):
      min_idx =  i
      for j in range(i+1, len(nums)):
        if nums[j] < nums[min_idx]:
          min_idx = j
      nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

print(Solution().selection_sort([4,3,-5,2,1]))