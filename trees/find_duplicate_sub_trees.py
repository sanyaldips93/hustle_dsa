# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        sub = defaultdict(list)
        res = []
        def dfs(node):
            if not node:
                return "null"
            word = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(sub[word]) == 1:
                res.append(node.val)
            sub[word].append(node)
            return word
        dfs(root)
        return res
    
node = TreeNode(2, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3)))
print(Solution().findDuplicateSubtrees(node))