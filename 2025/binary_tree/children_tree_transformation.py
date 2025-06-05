class Solution:
    def childSumTransformation(self, root):
        # Base case: if root is None or it's a leaf node, return
        if not root or (not root.left and not root.right):
            return

        child = 0
        if root.left:
            child += root.left.data
        if root.right:
            child += root.right.data

        # If children sum is greater, make root equal to children sum
        if child >= root.data:
            root.data = child
        else:
            # If root is greater, propagate root value down to children
            if root.left:
                root.left.data = root.data
            if root.right:
                root.right.data = root.data

        # Recurse down
        self.childSumTransformation(root.left)
        self.childSumTransformation(root.right)

        # After recursion, fix the current root again
        total = 0
        if root.left:
            total += root.left.data
        if root.right:
            total += root.right.data
        if root.left or root.right:
            root.data = total
