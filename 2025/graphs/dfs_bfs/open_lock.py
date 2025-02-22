from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visit = set(deadends)
        visit.add("0000")
        q = deque()
        q.append(["0000", 0])

        def children(node):
            res = []
            for i in range(4):
                nxt1 = str((int(node[i]) + 1) %10)
                nxt2 = str((int(node[i]) - 1 + 10) %10)
                res.append(node[:i] + nxt1 + node[i+1:])
                res.append(node[:i] + nxt2 + node[i+1:])
            return res
        
        while q:
            node, turns = q.popleft()
            if node == target:
                return turns
            for child in children(node):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
        
        return -1