from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        cur = root
        while True:
            tmp = cur
            if cur.val > val:
                cur = cur.left
                if not cur:
                    tmp.left = TreeNode(val)
                    break
            else:
                cur = cur.right
                if not cur:
                    tmp.right = TreeNode(val)
                    break
        return root

class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        def dfs(node):
            if node.val > val:
                if node.left: dfs(node.left)
                else:
                    node.left = TreeNode(val)
                    return
            elif node.val < val:
                if node.right: dfs(node.right)
                else:
                    node.right = TreeNode(val)
                    return
        dfs(root)
        return root