# https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

from typing import List
from collections import deque

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        if start == end:  # ✅ Edge case check
            return 0 
        
        q = deque()
        q.append([0, start])
        dist = [float("inf")] * 100000
        MOD = 100000
        dist[start] = 0
        
        while q:
            steps, node = q.popleft()
            for num in arr:
                new_node = (node * num) % MOD
                if dist[new_node] == float("inf"):
                    dist[new_node] = steps+1
                    if new_node == end:
                        return steps+1
                    q.append([steps+1, new_node])
        
        return -1
    
print(Solution().minimumMultiplications([2,5,7],3,30))