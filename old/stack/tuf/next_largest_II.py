from typing import List

# This is circular

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums + nums
        stack = []
        res = [-1] * len(nums)
        
        for i in range(len(arr)):
            num = arr[i]
            while stack and stack[-1][0] < num:
                val, index = stack.pop()
                idx = index % len(nums)
                res[idx] = num
            stack.append([num, i])
        
        return res

print(Solution().nextGreaterElements([4, 5, 2, 10, 8]))