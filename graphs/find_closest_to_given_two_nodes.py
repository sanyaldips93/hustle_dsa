from collections import defaultdict, deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = defaultdict(list)
        for i, dst in enumerate(edges):
            adj[i].append(dst)
        
        def bfs(src, distMap):
            q = deque()
            q.append([src, 0])
            distMap[src] = 0
            while q:
                node, dist = q.popleft()
                for nei in adj[node]:
                    if nei not in distMap:
                        q.append([nei, dist+1])
                        distMap[nei] = dist + 1
        node1Dis = {}
        node2Dis = {}
        bfs(node1, node1Dis)
        bfs(node2, node2Dis)

        res = -1
        resDist = float("inf")
        for i in range(len(edges)):
            if i in node1Dis and i in node2Dis:
                dist = max(node1Dis[i], node2Dis[i])
                if dist < resDist:
                    res = i
                    resDist = dist
        
        return res
        