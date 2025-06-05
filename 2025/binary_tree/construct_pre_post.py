from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        val = postorder[-1]
        node = TreeNode(val)
        idx = inorder.index(val)
        node.left = self.buildTree(inorder[:idx], postorder[:idx])
        node.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return node