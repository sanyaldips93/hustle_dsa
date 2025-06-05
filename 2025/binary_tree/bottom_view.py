from collections import defaultdict, deque

class Solution:
    def bottomView(self, root):
        colmap = defaultdict(list)
        q = deque([[root, 0, 0]])
        while q:
            node, row, col = q.popleft()
            if node:
                colmap[col].append(node.data)
                if node.left: q.append([node.left, row+1, col-1])
                if node.right: q.append([node.right, row+1, col+1])
        
        return [colmap[x][-1] for x in sorted(colmap)]