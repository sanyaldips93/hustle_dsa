from collections import defaultdict, deque
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if rank[px] > rank[py]:
                par[py] = px
            elif rank[py] > rank[px]:
                par[px] = py
            else:
                par[py] = px
                rank[px] += 1

        emailToAcc = {}
        for i in range(len(accounts)):
            emails = accounts[i][1:]
            for email in emails:
                if email in emailToAcc:
                    union(emailToAcc[email], i)
                else:
                    emailToAcc[email] = i
        
        accToEmail = defaultdict(list)
        for email in emailToAcc:
            account = emailToAcc[email]
            pac = find(account)
            accToEmail[pac].append(email)
        
        res = []
        for i in range(len(accToEmail)):
            res.append([accounts[i][:1]] + accToEmail[i])
        
        return res


print(Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))