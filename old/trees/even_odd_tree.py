from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            length = len(q)
            maxval = float("-inf")
            minval = float("inf")
            for _ in range(length):
                node = q.popleft()
                if level%2 == 0:
                    if node.val <= maxval or node.val%2 != 1:
                        return False
                    maxval = max(maxval, node.val)
                else:
                    if node.val >= minval or node.val%2 != 0:
                        return False
                    minval = min(minval, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True