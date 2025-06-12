from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()
        self.res = False
        def dfs(node):
            if not node: return
            val = k - node.val
            if val in hashset:
                self.res = True
                return
            else:
                hashset.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res