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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
  let res = [];
  function dfs(root, str="") {
      if(!root) return null;
      str += root.val + "->";
      dfs(root.left, str);
      dfs(root.right, str);
      if(!root.left && !root.right) {
          res.push(str.slice(0,-2));
      }
  }
  dfs(root);
  return res;
};