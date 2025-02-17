from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr = image[sr][sc]

        def dfs(r, c, curr):
            if image[r][c] == curr:
                image[r][c] = color
            
                if (r >= 1):
                    dfs(r-1, c, curr)
                if (c >= 1):
                    dfs(r, c-1, curr)
                if (r+1 < len(image)):
                    dfs(r+1, c, curr)
                if (c+1 < len(image[0])):
                    dfs(r, c+1, curr)

        if curr != color:
            dfs(sr, sc, curr)
        
        return image

print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))