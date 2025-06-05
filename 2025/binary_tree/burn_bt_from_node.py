from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        node_map = {}
        q = deque()
        q.append(root)
        parent[root] = root
        while q:
            node = q.popleft()
            node_map[node.val] = node
            if node.left:
                q.append(node.left)
                parent[node.left] = node
            if node.right:
                q.append(node.right)
                parent[node.right] = node
        
        start = node_map[start]
        count = 0
        q = deque()
        q.append(start)
        visit = set()
        visit.add(start)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if parent[node] and parent[node] not in visit:
                    q.append(parent[node])
                    visit.add(parent[node])
                if node.left and node.left not in visit:
                    q.append(node.left)
                    visit.add(node.left)
                if node.right and node.right not in visit:
                    q.append(node.right)
                    visit.add(node.right)
            if q:
                count += 1
        
        return count