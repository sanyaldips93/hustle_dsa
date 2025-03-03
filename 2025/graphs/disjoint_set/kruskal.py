from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        
        # create edges
        edges = []
        for src in range(len(adj)):
            for des, wt in adj[src]:
                edges.append([wt, src, des])
        edges.sort(key= lambda x:x[0])
        
        # disjoint set
        par = [i for i in range(V)]
        rank = [1] * V
        
        def find(x):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]
            
        def unionset(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if rank[x] > rank[y]:
                par[y] = x
            elif rank[y] > rank[x]:
                par[x] = y
            else:
                par[y] = x
                rank[x] += 1
        
        # kruskal's
        mst = 0
        for wt, src, des in edges:
            if find(src) != find(des):
                mst += wt
                unionset(src, des)
        
        return mst