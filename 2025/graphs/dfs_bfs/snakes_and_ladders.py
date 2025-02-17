from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visit = set()
        board.reverse()

        def inttopos(square):
            r = (square-1) // n
            c = (square-1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]
        
        q = deque()
        q.append([1, 0]) # square, moves
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nsquare = square + i
                r, c = inttopos(nsquare)
                if board[r][c] != -1:
                    nsquare = board[r][c]
                if nsquare == n * n:
                    return moves + 1
                if nsquare not in visit:
                    visit.add(nsquare)
                    q.append([nsquare, moves+1])
        return -1