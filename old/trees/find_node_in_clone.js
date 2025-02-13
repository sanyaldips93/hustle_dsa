/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} original
 * @param {TreeNode} cloned
 * @param {TreeNode} target
 * @return {TreeNode}
 */

// in order
var getTargetCopyInOrder = function(original, cloned, target) {
  let res = null;
  function dfs(t1, t2) {
      if(!t1) return;
      dfs(t1.left, t2.left)
      if(t1 === target) {res = t2; return;}
      dfs(t1.right, t2.right);
  }
  dfs(original, cloned);
  return res;
};

// pre order
var getTargetCopy = function(original, cloned, target) {
  function dfs(t1, t2) {
      if(!t1) return;
      if(t1 === target) return t2;
      return dfs(t1.left, t2.left) || dfs(t1.right, t2.right);
  }
  return dfs(original, cloned);
};