# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            # split and update
            lm = dfs(root.left)
            rm = dfs(root.right)
            lm = max(lm, 0)
            rm = max(rm, 0)
            res[0] = max(res[0], root.val + lm + rm)

            # return the value if not split
            return root.val + max(lm, rm)
        dfs(root)
        return res[0]