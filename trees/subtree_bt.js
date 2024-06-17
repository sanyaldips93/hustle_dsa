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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(s, t) {
  //edge cases
  if (!t) return true;
  if (!s) return false;
  if(sameTree(s, t)) return true;
  return (isSubtree(s.left, t) || isSubtree(s.right, t));

};

function sameTree(s, t) {
  if(!s && !t) return true;
  if((!s || !t) || s.val != t.val) return false;
  return (sameTree(s.left, t.left) && sameTree(s.right, t.right));
}