from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        
        return res

print(Solution().permute([1,2,3]))
    
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return  # backtracking

        for i in range(len(nums)):
            num = nums.pop(i)
            self.dfs(nums, path + [num], res)
            nums.insert(i, num)  # Backtrack by inserting the element back to its original position
'''