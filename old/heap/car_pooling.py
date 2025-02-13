import heapq
from typing import List

# Solution 1
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []
        for i in range(len(trips)):
            pax, fromt, tot = trips[i]
            arr.extend([(fromt, pax), (tot, -pax)])
        arr.sort()
        curpax = 0
        for des, pax in arr:
            curpax += pax
            if curpax > capacity:
                return False
        return True
    
# Solution 2
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        trips.sort(key = lambda t:t[1])
        curpax = 0

        for i in range(len(trips)):
            pax, start, end = trips[i]
            while heap and heap[0][0] <= start:
                curpax -= heap[0][1]
                heapq.heappop(heap)
            curpax += pax
            if curpax > capacity:
                return False
            heapq.heappush(heap, [end, pax])
        return True