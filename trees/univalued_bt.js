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
 * @return {boolean}
 */
var isUnivalTree = function(root) {
  let val = root.val;
  let res = null;
  dfs(root);
  return res;
  function dfs(root) {
      if(!root) return;
      if(root.val !== val) res = false;
      dfs(root.left);
      dfs(root.right);
  }

};