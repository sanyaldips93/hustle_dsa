from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][0] > heights[i]:
                height, idx = stack.pop()
                val = (i - idx) * height
                area = max(area, val)
                index = idx
            stack.append([heights[i], index])

        length = len(heights)
        for item in stack:
            height, idx = item
            area = max(area, ((length - idx) * height))
        
        return area
    
print(Solution().largestRectangleArea([2,1,5,6,2,3]))