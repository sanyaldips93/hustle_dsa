from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]

        def dfs(r, c, color):
            if image[r][c] == color:
                image[r][c] = newColor
            
                if (r >= 1):
                    dfs(r-1, c, color)
                if (c >= 1):
                    dfs(r, c-1, color)
                if (r+1 < len(image)):
                    dfs(r+1, c, color)
                if (c+1 < len(image[0])):
                    dfs(r, c+1, color)
            

        if color != newColor:
            dfs(sr, sc, color)
        
        return image
        