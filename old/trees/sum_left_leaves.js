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
var sumOfLeftLeaves = function(root) {
  let sum = 0;
  function dfs(root, str="") {
      if(!root) return;
      if(!root.left && !root.right) {
          if(str==="L") {
              sum += root.val;
          } 
          return;
      }
      dfs(root.left, "L");
      dfs(root.right, "R");
  }
  dfs(root);
  return sum;
};