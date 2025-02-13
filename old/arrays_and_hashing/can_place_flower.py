from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arr = [0] + flowerbed + [0]
        for i in range(1, len(arr)-1):
            if arr[i-1] == 0 and arr[i] == 0 and arr[i+1] == 0:
                arr[i] = 1
                n -= 1
        return n <= 0
    
# it can be solved without creating a new array and assuming the values of -1 and len + 1 to be 0s.