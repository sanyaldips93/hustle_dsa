function Node(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var lowestCommonAncestor = function(root, p, q) {
  let cur = root;
  while(cur) {
      if(p.val > cur.val && q.val > cur.val) {
          cur = cur.right;
      } else if(p.val < cur.val && q.val < cur.val) {
          cur = cur.left;
      } else {
          return cur;
      }
  }
};

const root = new Node(1, new Node(2), new Node(3));
console.log(lowestCommonAncestor(root, root, root.left));
