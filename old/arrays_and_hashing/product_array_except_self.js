// Solution 1 -> O(n^2)
var productExceptSelf = function(nums) {
  const res = [];
  for(let i=0; i<nums.length; i++) {
      let tempProduct = 1;
      for(let j=0; j<nums.length; j++) {
          if(i!=j) {
              tempProduct *= nums[j];
          }
      }
      res.push(tempProduct);
  }
  return res;
};

// Solution 2 -> O(n)
var productExceptSelf = function(nums) {
  const forwardMovingArr = new Array(nums.length).fill(1);
  const backwardMovingArr = new Array(nums.length).fill(1);
  const res = [];
  for(let i=1; i<nums.length; i++) {
      forwardMovingArr[i] = forwardMovingArr[i-1] * nums[i-1];
  }
  for(let i=nums.length-2; i>=0; i--) {
      backwardMovingArr[i] = backwardMovingArr[i+1] * nums[i+1];
  }
  for(let i=0; i<nums.length; i++) {
      res.push(forwardMovingArr[i] * backwardMovingArr[i]);
  }
  return res;
};