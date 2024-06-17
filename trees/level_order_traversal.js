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
 * @return {number[][]}
 */
var levelOrder = function(root) {
  if(!root) return [];
  let res = [];
  let q = [root];
  while(q.length) {
      let len = q.length;
      let iRes = [];
      while(len) {
          let node = q.shift();
          iRes.push(node.val);
          node.left ? q.push(node.left) : '';
          node.right ? q.push(node.right) : '';
          len--;
      }
      res.push(iRes);
  }
  return res;
};