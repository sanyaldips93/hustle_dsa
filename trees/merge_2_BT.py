# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(n1, n2, r=None):
            if not n1 and not n2:
                return None
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            r = TreeNode(v1+v2)
            r.left = dfs(n1.left if n1 else None, n2.left if n2 else None, r)
            r.right = dfs(n1.right if n1 else None, n2.right if n2 else None, r)
            return r
        return dfs(root1, root2)
            