'''
Here's one way to interpret the goal: 
the only operation that we can run on the array transfers a unit toward elements on the left without affecting the overall sum. 
If you think about each array entry as a pile of rocks, 
the only allowed operation is to take a rock from one pile and move it to the pile on its left. 
The goal of the problem is to rearrange the rocks by applying this operation as many times as you want to make it 
so that the tallest pile is as low as possible.
'''

import math
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, math.ceil(total / (i + 1)))
        return res