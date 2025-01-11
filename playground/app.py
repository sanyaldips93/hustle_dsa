from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, arr):
            if i == len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()
            dfs(i+1, arr)
        dfs(0, [])
        return res

print(Solution().subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]