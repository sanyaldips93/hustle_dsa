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
var averageOfLevels = function(root) {
  let q = [root];
  let res = [];
  while(q.length) {
      let len = q.length;
      let curAvg = 0;
      for(let i=0; i<len; i++) {
          const node = q.shift();
          curAvg += node.val;
          node.left? q.push(node.left) : null;
          node.right? q.push(node.right) : null;
      }
      curAvg /= len;
      res.push(curAvg);
  }
  return res;
};