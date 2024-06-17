# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nxt = root, root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root
    
# Loop 1
# cur = 1, nxt = 2;
# 2.next = 3; 1 = 1.next = None; cur = 2, nxt = 4;
# Loop 2, cur = 2, nxt = 4
# 4.next = 5, 5.next = 6; cur = 2.next = 3
# Loop 3, cur = 3, nxt = 4
# 6.next = 7, cur = 4, nxt = None ... Loop breaks.