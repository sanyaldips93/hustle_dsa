#  NUMBER OF CONENCTED COMPONENTS IN UNDIRECTED GRAPH

class Solution:
  def countComponents(self, n, edges):
    par = [i for i in range(n)]
    rank = [1] * n

    def find(n):
      res = n
      while res != par[res]:
        par[res] = par[par[res]]
        res = par[res]
      return res
    
    def union(n1, n2):
      p1, p2 = find(n1), find(n2)
      if p1 == p2:
        return 0
      if rank[p1] > rank[p2]:
        par[p2] = p1
        rank[p1] += rank[p2]
      else:
        par[p1] = p2
        rank[p2] += rank[p1]
      return 1
    
    res = n
    for n1, n2 in range(res):
      res -= union(n1, n2)
    return res
  

# Solution 2
class Solution:
    def countComponents(self, n, edges) -> int:
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        res = 0
        def dfs(i, prev):
            if i in visit:
                return
            visit.add(i)
            for edg in adj[i]:
                if edg == prev:
                    continue
                dfs(edg, i)
        
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1
        
        return res
            