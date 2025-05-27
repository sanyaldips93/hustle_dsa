from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = []
        res = []
        for i in range(1, 10):
            arr.append(i)
        def dfs(idx, cur, temp):
            if len(cur) == k and temp == n:
                res.append(cur.copy())
                return
            
            if idx >= 9 or temp > n:
                return
            
            cur.append(arr[idx])
            dfs(idx+1, cur, temp+arr[idx])
            cur.pop()
            dfs(idx+1, cur, temp)
        
        dfs(0, [], 0)
        return res

print(Solution().combinationSum3(3, 7))