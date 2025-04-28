from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix[0]), len(matrix)
        height = [0] * n
        maxval = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != '0': height[j] += int(matrix[i][j])
                else: height[j] = 0
            maxval = max(maxval, self.largestRectangleArea(height))
        return maxval

    
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        i, maxarea = 0, 0
        while i < n:
            index = i
            while stack and stack[-1][0] > heights[i]:
                h, idx = stack.pop()
                maxarea = max(maxarea, h*(i-idx))
                index = idx
            stack.append([heights[i], index])
            i += 1
        m = len(stack)
        for i in range(m-1,-1,-1):
            h, idx = stack[i]
            maxarea = max(maxarea, h*(n-idx))
        return maxarea