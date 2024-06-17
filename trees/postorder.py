# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# using 1 stack
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        res = []
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
    
# using 2 stacks
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack1 = []
        stack2 = []
        res = []
        if not root: return []
        stack1.append(root)
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        while stack2:
            res.append(stack2.pop().val)
        return res