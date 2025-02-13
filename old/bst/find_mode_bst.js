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
 * @return {number[]}
 */
var findMode = function(root) {
  let cur = null;
  let cunt = 0;
  let max = Number.MIN_SAFE_INTEGER;
  let modes = [];
  function dfs(root) {
      if(!root) return null;
      dfs(root.left);
      if(root.val === cur) {
          cunt++;
      } else {
          cur = root.val;
          cunt = 1;
      }
      if(cunt > max) {
          max = cunt;
          modes = [cur];
      } else if(cunt === max) {
          modes.push(cur);
      }
      dfs(root.right);
  }
  dfs(root);
  return modes;
};