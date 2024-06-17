from typing import List


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        pascal = []
        
        for i in range(1, n+1):
            pascal.append([0]*i)
        
        for i in range(0, n):
            for j in range(0, i+1):
                if j == 0 or j == i:
                    pascal[i][j] = 1
                else:
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
                
        return pascal