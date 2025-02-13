from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = { i:[] for i in range(n) }
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)
        def dfs(cur, prev):
            time = 0
            for edge in adj[cur]:
                if edge == prev:
                    continue
                childTime = dfs(edge, cur)
                if childTime or hasApple[edge]:
                    time += 2 + childTime
            return time
        return dfs(0, -1)

Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False])