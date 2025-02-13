from typing import List

# Solution 1
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hashset = { s for s in nums }
        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in hashset else res
            
            res = backtrack(i + 1, cur)
            if res: return res
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res: return res
        
        return backtrack(0, ["0" for s in nums])
    
# Solution 2
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        n = len(nums)
        alpha = set()

        for i in nums:
            alpha.add(int(i, 2))

        for j in range(2**n):
            if j not in alpha:
                ans = bin(j)[2:]
                return ans if len(ans) == n else '0' * (n - len(ans)) + ans