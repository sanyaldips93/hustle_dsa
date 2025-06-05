from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res[::-1]
    
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        cur, stack = root, []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                temp = stack[-1].right
                if temp == None:
                    temp = stack.pop()
                    res.append(temp.val)
                    while stack and stack[-1].right == temp:
                        temp = stack.pop()
                        res.append(temp.val)
                else:
                    cur = temp
        return res