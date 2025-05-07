from typing import List


class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        
        for i in range(n):
            for j in range(n//2):
                arr[i][j], arr[i][n-j-1] = arr[i][n-j-1], arr[i][j]

print(Solution().rotate([[1,2,3], [4,5,6], [7,8,9] ]))