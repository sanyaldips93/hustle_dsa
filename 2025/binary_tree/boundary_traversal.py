class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        res = []
        if not root: return res
        res.append(root.data)
        
        def addLeftBoundary(node):
            if not node: return
            if not node.left and not node.right: return
            res.append(node.data)
            if node.left: return addLeftBoundary(node.left)
            else: return addLeftBoundary(node.right)
            
        reverseres = []
        def addRightBoundary(node):
            if not node: return
            if not node.left and not node.right: return
            reverseres.append(node.data)
            if node.right: return addRightBoundary(node.right)
            else: return addRightBoundary(node.left)
        
        def addLeaves(node):
            if not node: return
            if node == root:
                addLeaves(node.left)
                addLeaves(node.right)
                return
            if not node.left and not node.right: 
                res.append(node.data)
                return
            addLeaves(node.left)
            addLeaves(node.right)
        
        
        addLeftBoundary(root.left)
        addLeaves(root)
        addRightBoundary(root.right)
        
        return res + reverseres[::-1]