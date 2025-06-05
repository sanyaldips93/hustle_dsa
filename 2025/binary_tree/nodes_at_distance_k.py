from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = deque()
        q.append(root)
        parent = {}
        parent[root] = root
        while q:
            node = q.popleft()
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        
        q = deque()
        q.append(target)
        dist = 0
        visit = set()
        visit.add(target)
        while q:
            if dist == k:
                break
            for i in range(len(q)):
                node = q.popleft()
                if parent[node] and parent[node] not in visit:
                    visit.add(parent[node])
                    q.append(parent[node])
                if node.left and node.left not in visit:
                    visit.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visit:
                    visit.add(node.right)
                    q.append(node.right)
            dist += 1
        
        return [node.val for node in q]