from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        v1, mid, v2, prev = None, None, None, None
        def dfs(node):
            nonlocal v1, mid, v2, prev
            if not node: return
            dfs(node.left)
            if prev and node.val < prev.val:
                if not v1:
                    v1 = prev
                    mid = node
                else:
                    v2 = node
            prev = node
            dfs(node.right)
        dfs(root)
        if v2:
            v1.val, v2.val = v2.val, v1.val
        else:
            v1.val, mid.val = mid.val, v1.val