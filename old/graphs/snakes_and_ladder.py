from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visit = set()
        board.reverse()
        
        def inttopos(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2:
                col = n - 1 - col
            return [row, col]
        
        q = deque()
        q.append([1, 0]) # square, moves
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                newsquare = square + i
                r, c = inttopos(newsquare)
                if board[r][c] != -1:
                    newsquare = board[r][c]
                if newsquare == n * n:
                    return moves + 1
                if newsquare not in visit:
                    visit.add(newsquare)
                    q.append([newsquare, moves + 1])
        return -1

        