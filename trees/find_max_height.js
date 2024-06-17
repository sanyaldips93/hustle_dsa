function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

var maxHeightDfs = function(root) {
  if(root === null) return 0;
  return 1 + Math.max(maxHeightDfs(root.left), maxHeightDfs(root.right));
}

var maxHeightBfs = function(root) {
  let level = 0;
  let q = [root];
  while(q.length) {
    for(let i=0; i<q.length; i++) {
      let node = q.shift();
      node.left ? q.push(node.left) : null;
      node.right ? q.push(node.right) : null;
    }
    level += 1;
  }
  return level;
}

var maxDepthDfsItr = function(root) {
  let q = [[root,1]];
  res = 0;
  while(q.length) {
    let [node, d] = q.pop();
    if(node) {
      res = Math.max(res, d);
      q.push([node.right, d + 1]);
      q.push([node.left, d + 1]);
    }
  }
  return res;
};