class Solution:
    def findPath(self, m, n):
        # code here
        visit = set()
        res = []
        
        def dfs(r, c, path):
            if r == n-1 and c == n-1 and m[r][c] == 1 and path != "":
                return res.append(path)
            
            if r < 0 or c < 0 or r >= n or c >= n or (r, c) in visit or m[r][c] != 1:
                return
            
            visit.add((r, c))
            dfs(r+1, c, path + "D")
            dfs(r-1, c, path + "U")
            dfs(r, c+1, path + "R")
            dfs(r, c-1, path + "L")
            visit.remove((r, c))
            
        if m[0][0] == 1:
            dfs(0, 0, "")

        
        return res if res != [] else -1

print(Solution().findPath([[1,0,0,0], [1,1,0,1], [1,1,0,0], [0,1,1,1]], 4))