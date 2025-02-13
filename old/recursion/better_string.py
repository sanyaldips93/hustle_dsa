class Solution:
    def betterString(self, str1, str2):
        # Code here
        res1 = set()
        res2 = set()
    
        def dfs(i, tmp, res, stri):
            if i == len(stri):
                res.add(tmp)
                return
            if i >= len(stri):
                return
            
            dfs(i+1, tmp + stri[i], res, stri)
            dfs(i+1, tmp, res, stri)
              
        dfs(0, "", res1, str1)
        dfs(0, "", res2, str2)
          
        return str1 if len(res1) >= len(res2) else str2