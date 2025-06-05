from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res
        q = deque([root])
        while q:
            inner = []
            for _ in range(len(q)):
                node = q.popleft()
                inner.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(inner[::-1] if len(res)%2 else inner)
        return res