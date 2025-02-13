// T - 0(n), M - O(n)
var maxSlidingWindow = function(nums, k) {
  const output = [];
  const q = [];
  let l = 0, r = 0;
  while(r < nums.length) {
      while(q && nums[q[q.length-1]] < nums[r]) {
          q.pop();
      }
      q.push(r);

      if(q[0] < l) {
          q.shift();
      }

      if(r+1-l == k) {
          output.push(nums[q[0]]);
          l += 1;
      }
      r += 1;
  }
  return output;
};