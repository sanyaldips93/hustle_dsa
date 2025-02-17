class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        map = {node: Node(node.val)}
        q = deque([node])
        while q:
            node1 = q.popleft()
            clone = map[node1]
            for nei in node1.neighbors:
                if nei not in map:
                    map[nei] = Node(nei.val)
                    q.append(nei)
                clone.neighbors.append(map[nei])
        return map[node]