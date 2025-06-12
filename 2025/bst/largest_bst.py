class Solution:
    def largestBst(self, root):
        self.maxi = 0
        def dfs(node):
            if not node:
                return [True, 0, float("-inf"), float("inf")]
            lisbst, lsize, lmax, lmin = dfs(node.left)
            risbst, rsize, rmax, rmin = dfs(node.right)
            
            if lisbst and risbst and lmax < node.data < rmin:
                size = lsize + rsize + 1
                minval = min(lmin, node.data)
                maxval = max(rmax, node.data)
                self.maxi = max(self.maxi, size)
                return [True, size, maxval, minval]
            
            return [False, max(lsize, rsize), float("inf"), float("-inf")]
        
        dfs(root)
        return self.maxi