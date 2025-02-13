
function Node(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
  const str1 = [];
  const str2 = [];
  function dfs(root, str) {
      if(!root) return null;
      if(!root.left && !root.right) {
          str.push(root.val);
      }
      dfs(root.left, str);
      dfs(root.right, str);
  };
  dfs(root1, str1);
  dfs(root2, str2);
  if(str1.join(',') === str2.join(',')) return true;
  return false;
};

const root1 = new Node(1, new Node(2), new Node(3));
const root2 = new Node(1, new Node(2), new Node(3));
console.log(leafSimilar(root1, root2));
