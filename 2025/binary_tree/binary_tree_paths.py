from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root: return res
        def dfs(node, cur):
            if not node:
                return
            cur.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(cur.copy()))
                cur.pop()
                return
            dfs(node.left, cur)
            dfs(node.right, cur)
            cur.pop()
        dfs(root, [])
        return res