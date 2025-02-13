from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # binary tree must have one parent node
        hashParent = set(leftChild + rightChild)
        hashParent.discard(-1)
        if len(hashParent) == n:
            return False

        root = -1
        for i in range(n):
            if i not in hashParent:
                root = i
                break
        # bt must contain no cycles and be connected
        visit = set()
        def dfs(i):
            if i == -1:
                return True
            if i in visit:
                return False
            visit.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        return dfs(root) and len(visit) == n
    
# Input : n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]