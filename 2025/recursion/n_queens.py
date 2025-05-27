from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posd, negd = set(), set(), set()
        res = []
        board = [["."] * n for _ in range(n)]
        def backtrack(i):
            if i == n: res.append(["".join(row) for row in board])
            for j in range(n):
                if j in cols or i+j in posd or i-j in negd: continue

                cols.add(j)
                posd.add(i+j)
                negd.add(i-j)
                board[i][j] = "Q"

                backtrack(i+1)

                cols.remove(j)
                posd.remove(i+j)
                negd.remove(i-j)
                board[i][j] = "."
        
        backtrack(0)
        return res