# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
          return TreeNode(val)
        cur = root
        while True:
          tmp = cur
          if(cur.val < val):
              cur = cur.right
              if not cur:
                  tmp.right = TreeNode(val)
                  return root
          else:
              cur = cur.left
              if not cur:
                  tmp.left = TreeNode(val)
                  return root