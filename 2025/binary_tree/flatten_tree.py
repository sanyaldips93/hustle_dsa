from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def dfs(node):
            nonlocal prev
            if not node: return None
            dfs(node.right)
            dfs(node.left)

            node.left = None
            node.right = prev
            prev = node
        dfs(root)

class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [root]
        if not root:
            return
        while stack:
            cur = stack.pop()
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)

            if stack:
                cur.right = stack[-1]
            cur.left = None