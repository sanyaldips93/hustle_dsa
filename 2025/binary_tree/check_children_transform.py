class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isSumProperty(self, root):
        def dfs(node):
            if not node or (not node.left and not node.right): 
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            leftVal = node.left.data if node.left else 0 
            rightVal = node.right.data if node.right else 0
            
            return (node.data == rightVal + leftVal) and left and right
        
        return 1 if dfs(root) else 0
            