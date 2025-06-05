from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, -1]
            [bool1, h1] = dfs(node.left)
            [bool2, h2] = dfs(node.right)

            bool3 = abs(h1-h2) <= 1 and bool1 and bool2
            return [bool3, 1+max(h1, h2)]
        return dfs(root)[0]