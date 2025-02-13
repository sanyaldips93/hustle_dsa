# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, p: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not p and not r:
            return True
        if (not p or not r) or (p.val != r.val):
            return False
        a = self.flipEquiv(p.left, r.left) and self.flipEquiv(p.right, r.right)
        return a or self.flipEquiv(p.left, r.right) and self.flipEquiv(p.right, r.left)