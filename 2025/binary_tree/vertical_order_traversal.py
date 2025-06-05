from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        q = deque([[root, 0, 0]]) # node, level, vertical line
        while q:
            node, row, col = q.popleft()
            if node:
                nodes.append([col, row, node.val])
                q.append([node.left, row+1, col-1])
                q.append([node.right, row+1, col+1])
        
        nodes.sort()
        colmap = defaultdict(list)
        for col, row, val in nodes:
            colmap[col].append(val)
        
        return [colmap[x] for x in sorted(colmap)]