from collections import defaultdict
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

            if x != y:
                if rank[px] > rank[py]:
                    par[py] = px
                elif rank[py] > rank[px]:
                    par[px] = py
                else:
                    par[py] = px
                    rank[px] += 1
        
        # map account to email
        emailToAcc = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email in emailToAcc:
                    union(emailToAcc[email], i)
                else:
                    emailToAcc[email] = i
        
        # attach emails to account
        accToEmail = defaultdict(list)
        for email in emailToAcc:
            account = emailToAcc[email]
            pi = find(account)
            if email not in accToEmail[pi]:
                accToEmail[pi].append(email)
        
        # finally merge the dataset (account name + emails)
        res = []
        for account in accToEmail:
            name = accounts[account][0]
            res.append([name] + sorted(accToEmail[account]))
    
print(Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))