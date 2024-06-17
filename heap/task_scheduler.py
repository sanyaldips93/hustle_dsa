from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    q.append([cnt, time + n])            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time