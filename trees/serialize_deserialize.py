# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(root):
            if not root:
                return res.append("N")
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
print(deser.deserialize([1, 2, "N", "N", 3, 4, "N", "N", 5, "N", "N"]))