# https://leetcode.com/problems/satisfiability-of-equality-equations

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        chars = set()
        for equation in equations:
            ch1 = equation[0]
            ch2 = equation[-1]
            chars.add(ch1)
            chars.add(ch2)

        par = {}
        for ch in chars:
            par[ch] = ch
        rank = {}
        for ch in chars:
            rank[ch] = 0
        

        def find(x):
            if x == par[x]: return x
            par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if rank[px] > rank[py]:
                par[py] = px
            elif rank[py] > rank[px]:
                par[px] = py
            else:
                par[py] = px
                rank[px] += 1
        
        i = 0
        while i<2:
            for equation in equations:
                ch1, ch2 = equation[0], equation[-1]
                op1, op2 = equation[1], equation[2]
                if op1 == op2:
                    union(ch1, ch2)
                else:
                    px, py = find(ch1), find(ch2)
                    if px == py: return False
            i += 1
        
        return True

print(Solution().equationsPossible(["a==b","b!=a"]))