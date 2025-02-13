import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        avail = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(avail)
        unavail = []
        t = 0
        for i in range(len(tasks)):
            # if we ever advance time, then t will be ahead of i. so we need to take the max(t, i)
            t = max(t, i)

            # forward time if necessary
            if len(avail) == 0:
                t = unavail[0][0]
            
            # check if there are servers in unavail that can be made available
            while unavail and t >= unavail[0][0]:
                time, weight, idx = heapq.heappop(unavail)
                heapq.heappush(avail, (weight, idx))
            
            # now take an available server and assign it some task
            weight, idx = heapq.heappop(avail)
            res.append(idx)
            heapq.heappush(unavail, (t + tasks[i], weight, idx))
        return res
    
print(Solution().assignTasks([3,3,2], [1,2,4,3,2,2]))