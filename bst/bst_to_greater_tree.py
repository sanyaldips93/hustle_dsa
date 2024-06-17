# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = 0
        def dfs(node):
            if not node:
                return
            nonlocal cur
            dfs(node.right)
            tmp = node.val
            node.val += cur
            cur += tmp
            dfs(node.left)
        dfs(root)
        return root