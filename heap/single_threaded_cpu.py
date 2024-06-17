import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda k : k[0])
        res, minheap = [], []
        i, time = 0, tasks[0][0]
        
        while i < len(tasks) or minheap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not minheap:
                time = tasks[i][0]

            else:
                [proctime, idx] = heapq.heappop(minheap)
                time += proctime
                res.append(idx)
        
        return res

print(Solution().getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]))