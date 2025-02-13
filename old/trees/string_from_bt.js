
function Node(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @return {string}
 */
var tree2str = function(root) {
  let str = [];
  function dfs(root) {
      if(!root) return null;
      str.push('(');
      str.push(root.val);
      if(!root.left && root.right) {
          str.push('()');
      }
      dfs(root.left);
      dfs(root.right);
      str.push(')');
  }
  dfs(root)
  return str.join('').slice(1,-1);
};

const root = new Node(1, new Node(2), new Node(3));
console.log(tree2str(root));