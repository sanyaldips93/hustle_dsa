 function Node(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findSecondMinimumValue = function(root) {
  let arr = [Number.MAX_SAFE_INTEGER,Number.MAX_SAFE_INTEGER];
    function dfs(root) {
        root.left ? dfs(root.left) : '';
        root.right ? dfs(root.right) : '';
        insertInArr(root);
    }
    dfs(root);
    function insertInArr(node) {
        if(node.val === arr[0]) {
          return;
        } else if(node.val < arr[0]) {
          if(arr[0] < arr[1]) arr[1] = arr[0];
            arr[0] = node.val;
        } else if(node.val < arr[1]) {
            arr[1] = node.val;
        }
    }
    if(arr[1] === Number.MAX_SAFE_INTEGER) return -1;
    return arr[1];
};


let root = new Node(5);
let left = new Node(8);
let right = new Node(5);
// let leftleft = new Node(5);
// let rightright = new Node(7);

root.left = left;
root.right = right;
// right.left = leftleft;
// right.right = rightright;

console.log(findSecondMinimumValue(root));
