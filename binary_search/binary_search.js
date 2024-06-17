// Time - O(n), Memory - O(logn)
var search = function(nums, target) {
  let left = 0;
  let right = nums.length - 1;
  while(left<=right) {
      let midVal = Math.trunc((left+right)/2);
      if(nums[midVal] === target) return midVal;
      if(nums[midVal] > target) {
          right--;
      } else {
          left++;
      }
  }
  return -1;
};