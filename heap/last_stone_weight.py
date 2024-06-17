import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -1 * i for i in stones] # negation required for minheap
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: # since negative numbers are greater when positive is smaller
                heapq.heappush(stones, first - second) # this substraction would yield negative value always
            # no requirement of else, since equal first and second value would be destroyed
        stones.append(0)
        return abs(stones[0])