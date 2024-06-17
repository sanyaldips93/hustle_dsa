/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumRootToLeaf = function(root) {
  let res = [];
  function dfs(root, str="") {
      if(!root) return;
      if(!root.left && !root.right) {
          res.push(parseInt(str + root.val, 2));
          return;
      }
      str += root.val;
      dfs(root.left, str);
      dfs(root.right, str);
  }
  dfs(root);
  return res.reduce((a, c) => a + c,0);
};