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
var minDiffInBST = function(root) {
  let prev = null;
  let res = Number.POSITIVE_INFINITY;
  function dfs(root) {
      if(!root) return null;
      dfs(root.left);
      if(prev) {
          res = Math.min(res, root.val - prev.val);
      }
      prev = root;
      dfs(root.right);
  }
  dfs(root);
  return res;
};


