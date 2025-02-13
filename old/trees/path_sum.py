# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         res = [False]
#         def dfs(node, sum=0):
#             if not node:
#                 return None
#             sum += node.val
#             left = dfs(node.left, sum)
#             right = dfs(node.right, sum)
#             if not left and not right and sum == targetSum:
#                 res[0] = True
#             return node
            
#         dfs(root)
#         return res[0]
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = False
        if not root:
            return res
        def dfs(root, sum):
            nonlocal res
            if not root :
              if sum == targetSum:
                  res = True
              return
            dfs(root.left, sum + root.val)
            dfs(root.right, sum + root.val)
        dfs(root, 0)
        return res
    
node = TreeNode(1, TreeNode(2))

res = Solution().hasPathSum(node, 1)
print(res)