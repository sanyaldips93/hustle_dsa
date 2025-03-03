# Prim'a Algorithm

from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        heap = []
        src = 0
        heapq.heappush(heap, [0,src]) # cost, node, parent
        visit = set()
        # spanTree = []
        sum = 0
        
        while heap:
            cost, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            sum += cost
            # if parent != -1:
            #     spanTree.append([parent, node])
            for nei in adj[node]:
                des, wt = nei
                if des not in visit:
                    heapq.heappush(heap, [wt, des])
        
        
        return sum