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
 * @return {TreeNode}
 */
var increasingBST = function(root) {
  let dummy = new TreeNode();
  const ptr = dummy;
  function dfs(root) {
      if(!root) return null;
      dfs(root.left);
      dummy.right = new TreeNode(root.val);
      dummy = dummy.right;
      dfs(root.right);
      return;
  }
  dfs(root);
  return ptr.right; 
};