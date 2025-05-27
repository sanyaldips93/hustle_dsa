class Solution:
    def ratInMaze(self, maze):
        visit = set()
        res = []
        n = len(maze)
        def backtrack(r, c, cur):
            if r == n-1 and c == n-1:
                res.append("".join(cur.copy()))
                return
            
            if r < 0 or c < 0 or r >= n or c >= n or (r, c) in visit or maze[r][c] == 0:
                return
            
            visit.add((r, c))
            
            cur.append('D')
            backtrack(r+1, c, cur)
            cur.pop()
            
            cur.append('L')
            backtrack(r, c-1, cur)
            cur.pop()
            
            cur.append('R')
            backtrack(r, c+1, cur)
            cur.pop()
                        
            cur.append('U')
            backtrack(r-1, c, cur)
            cur.pop()
            
            
            visit.remove((r, c))
        
        if maze[0][0]: backtrack(0, 0, [])
        
        return res

# print(Solution().ratInMaze([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]))
print(Solution().ratInMaze([[1,1],[0,1]]))