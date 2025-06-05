from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def topView(self,root):
        colmap = defaultdict(int)
        q = deque([[root, 0, 0]])
        while q:
            node, row , col = q.popleft()
            if node:
                if not colmap[col]: colmap[col] = node.data
                if node.left: q.append([node.left, row+1, col-1])
                if node.right: q.append([node.right, row+1, col+1])
        
        return [colmap[x] for x in sorted(colmap)]