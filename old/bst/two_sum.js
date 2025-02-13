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
 * @param {number} k
 * @return {boolean}
 */
var findTarget = function(root, k) {
  let hash = {};
  function dfs(root) {
      if(!root) return false;
      let y = k - root.val;
      if(y in hash) return true;
      else hash[root.val] = true;
      return (dfs(root.left) || dfs(root.right));
  }
  return dfs(root);
};