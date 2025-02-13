class Solution:
  def bubble_sort(self, nums):
    swap = True
    while swap != False:
      tmp = 0
      for i in range(1, len(nums)):
        one, two = nums[i-1], nums[i]
        if one > two:
          nums[i-1], nums[i] = nums[i], nums[i-1]
          tmp += 1
      if tmp == 0:
        swap = False
    return nums

print(Solution().bubble_sort([4,3,1,5,2]))