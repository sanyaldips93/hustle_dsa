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
var rightSideView = function(root) {
  if(!root) return [];
  let res = [];
  let q = [root];
  while(q.length) {
      let len = q.length;
      while(len) {
          let node = q.shift();
          if(node.left) q.push(node.left);
          if(node.right) q.push(node.right);
          if(len === 1) res.push(node.val);
          len--;
      }
  }
  return res;
};