from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = [ i for i in range(len(accounts)) ]
        rank = [1] * len(accounts)
        
        def find(n):
            while n != par[n]:
                n = par[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        emailtoAcc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoAcc:
                    union(i, emailtoAcc[e])
                else:
                    emailtoAcc[e] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailtoAcc.items():
            leader = find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res
        