import heapq
from typing import List

'''
# Heaps
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [[arr[i] - x, arr[i]] for i in range(len(arr))]
        heapq.heapify(heap)
        res = []
        for j in range(k):
            [idx, element] = heapq.heappop(heap)
            res.append(element)
        return res
    
print(Solution().findClosestElements([1,2,3,4,5], 4, 3))
'''

# Binary Search / Sliding Window 
class Solution:
  def findClosestElements(self, arr: List[int], k: int, target: int) -> List[int]:
    left = 0
    right = len(arr) - 1

    while right - left >= k:
      if abs(arr[left] - target) > abs(arr[right] - target):
        left = left + 1
      else:
        right = right - 1

    return arr[left:left + k]
  
print(Solution().findKClosestElements([1,2,3,4,5], 3, 4))