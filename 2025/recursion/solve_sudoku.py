from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def canSolve(r, c, num):
            gr = (r // 3) * 3
            gc = (c // 3) * 3
            num = str(num)
            for i in range(0, 9):
                if board[i][c] == num: return False
                if board[r][i] == num: return False
                if board[gr + i//3][gc + i%3] == num: return False
            
            return True
        
        def solve():
            for i in range(0, 9):
                for j in range(0, 9):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            if canSolve(i, j, num):
                                board[i][j] = str(num)
                                if solve():
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        
        solve()