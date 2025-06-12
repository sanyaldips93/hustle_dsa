class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None 

class Solution:
    def findCeil(self,root, inp):
        ceil = -1
        while root:
            if root.key == inp:
                return root.key
            
            if root.key < inp:
                root = root.right
            else:
                ceil = root.key
                root = root.left
        return ceil


class Solution:
    def floor(self, root, x):
        floor = -1
        while root:
            if root.data == x:
                return root.data
            
            if  x < root.data:
                root = root.left
            else:
                floor = root.data
                root = root.right
        return floor