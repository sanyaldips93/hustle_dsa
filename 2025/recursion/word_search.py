from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        m = len(board)
        n = len(board[0])
        res = []
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or (r, c) in visit or board[r][c] != word[idx]:
                return False
            visit.add((r, c))
            idx += 1
            res = dfs(r+1, c, idx) or dfs(r-1, c, idx) or dfs(r, c+1, idx) or dfs(r, c-1, idx)
            visit.remove((r, c))
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))