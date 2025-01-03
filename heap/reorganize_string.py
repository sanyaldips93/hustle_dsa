from collections import Counter
import heapq
import math


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(heap)
        res = ""
        prev = None

        while heap or prev:
            if prev and not heap:
                return ""
            [cnt, char] = heapq.heappop(heap)
            cnt += 1
            res += char
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res
    
print(Solution().reorganizeString("abaa"))

class Solution2:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
    
        count = Counter(s)
        heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(heap)

        # edge case, if one char is more than half of the string, return    
        top = heap[0]
        if -top[0] > math.ceil(len(s)/2):   
            return ""
        
        res = ""
        while heap:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap) if heap else [0, ""]
            res += first[1] + second[1]
            if first[0] + 1 < 0:
                heapq.heappush(heap, [first[0]+1, first[1]])
            if second[0] + 1 < 0:
                heapq.heappush(heap, [second[0]+1, second[1]])
        return res