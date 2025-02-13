from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posd = set() # (r+c)
        negd = set() # (r-c)

        res = []
        board = [ ["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                return res.append(copy)

            for c in range(n):
                if c in cols or (r+c) in posd or (r-c) in negd:
                    continue
                
                cols.add(c)
                posd.add(r+c)
                negd.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res
    
print(Solution().solveNQueens(4))