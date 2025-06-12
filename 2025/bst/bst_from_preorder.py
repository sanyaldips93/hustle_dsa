from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(arr, bound):
            if len(arr) == 0 or arr[-1] > bound: return None
            val = arr.pop()
            node = TreeNode(val)
            node.left = dfs(arr, node.val)
            node.right = dfs(arr, bound)
            return node
        return dfs(preorder[::-1], float("inf"))
    
class Solution2:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        def dfs(arr, bound):
            if len(arr) == self.i or arr[self.i] > bound: return None
            val = arr[self.i]
            self.i += 1
            node = TreeNode(val)
            node.left = dfs(arr, node.val)
            node.right = dfs(arr, bound)
            return node
        return dfs(preorder, float("inf"))