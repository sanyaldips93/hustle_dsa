function Node(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function(root, x, y) {
  let d1 = [];
  let d2 = [];
  function dfs(root, p=-1, d=0) {
      if(!root) return;
      if(root.val === x) d1 = [d, p];
      if(root.val === y) d2 = [d, p];
      dfs(root.left, root.val, d+1);
      dfs(root.right, root.val, d+1);
  }
  dfs(root);
  return d1[0] === d2[0] && d1[1] !== d2[1]
};

const node = new Node(1, new Node(2, null, new Node(4)), new Node(3));
console.log(isCousins(node, 3, 4));
