from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append([root, 0])
        res = 0
        while q:
            mini = q[0][1] # The first index of the level, so this is gotta be the minimum.
            size = len(q)
            for i in range(size):
                node, idx = q.popleft()
                curidx = idx - mini # normalising the index by dividing mini from it.
                if i == 0: first = curidx # meaning the first item in the loop will always have the lowest index.
                if i == size-1: last = curidx # meaning the last item in the loop will always have the highest index.
                if node.left: q.append([node.left, curidx*2+1])
                if node.right: q.append([node.right, curidx*2+2])
            res = max(res, last - first + 1)
        return res