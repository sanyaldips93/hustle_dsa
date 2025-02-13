# Definition for a binary tree node.
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
          if not root:
            return None
          dfs(root.left)
          res.append(root.val)
          dfs(root.right)
        dfs(root)
        return res
    
node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)

res = Solution().inorderTraversal(node)
print(res)

class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            else:
                break
        return res
