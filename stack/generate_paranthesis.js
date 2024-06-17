// // Time - O(2^n), Memory - O(2^n)
var generateParenthesis = function(n) {
  const stack = [];
  const res = [];
  var backtrack = function(open, close) {
      if(open === n && close === n) {
          res.push(stack.join(''));
          return;
      }

      if(open < n) {
          stack.push('(');
          backtrack(open+1, close);
          stack.pop();
      }

      if(close < open) {
          stack.push(')');
          backtrack(open, close+1);
          stack.pop();
      }
  }

  backtrack(0,0);
  return res;
};

console.log(generateParenthesis(3));