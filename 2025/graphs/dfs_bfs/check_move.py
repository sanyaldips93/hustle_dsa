from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        direc = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

        def dfs(r, c, color, d):
            dr, dc = d
            nr, nc = dr + r, dc + c
            length = 1
            while (0 <= nr < rows and 0 <= nc < cols):
                length += 1
                if board[nr][nc] == '.':
                    return False
                if board[nr][nc] == color:
                    return length >= 3
                nr = nr + dr
                nc = nc + dc
            
            return False
        
        for dir in direc:
            if dfs(rMove, cMove, color, dir):
                return True
        
        return False