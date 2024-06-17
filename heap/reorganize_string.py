from collections import Counter
import heapq


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