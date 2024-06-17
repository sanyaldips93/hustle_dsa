import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, heap = "", []
        for cnt, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if cnt != 0:
                heapq.heappush(heap, [cnt, char])
        
        while heap:
            cnt, char = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                cnt2, char2 = heapq.heappop(heap)
                res += char2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(heap, [cnt2, char2])
            else:
                res += char
                cnt += 1
            if cnt:
                heapq.heappush(heap, [cnt, char])
        return res
    
print(Solution().longestDiverseString(7, 1, 0))