from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node, h):
            if not node: return
            res[0] = max(res[0], h)
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        dfs(root, 1)
        return res[0]