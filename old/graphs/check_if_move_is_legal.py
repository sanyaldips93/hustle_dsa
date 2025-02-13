from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        Rows, Cols = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]

        def isLegal(row, col, color, dir):
            dr, dc = dir
            row, col = row + dr, col + dc
            length = 1

            while(0 <= row < Rows and 0 <= col < Cols):
                length += 1
                if board[row][col] == '.':
                    return False
                if board[row][col] == color:
                    return length >= 3
                row, col = row + dr, col + dc
            return False
        
        for d in directions:
            if isLegal(rMove, cMove, color, d):
                return True
        return False

        