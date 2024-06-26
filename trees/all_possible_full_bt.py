# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1:[TreeNode()]}
        def backtrack(n):
            if n in dp:
                return dp[n]
            res = []
            for L in range(n):
                R = n - 1 - L
                leftTrees = backtrack(L)
                rightTrees = backtrack(R)

                for i in leftTrees:
                    for j in rightTrees:
                        res.append(TreeNode(0, i, j))
            dp[n] = res    
            return res
        return backtrack(n)