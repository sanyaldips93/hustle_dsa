from collections import defaultdict, deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
        # print(adj)
        q = deque([(headID, 0)])
        res = 0
        while q:
            id, time = q.popleft()
            res = max(res, time)
            for emp in adj[id]:
                q.append((emp, time + informTime[id]))
        return res

print(Solution().numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
