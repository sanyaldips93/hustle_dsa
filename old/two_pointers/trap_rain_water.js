// Solution 1 -> O(n) & O(n)
/*
var trap = function(height) {
  const maxLeftList = new Array(height.length).fill(0);
  const maxRightList = new Array(height.length).fill(0);
  let res = 0;
  let maxLeft = 0;
  let maxRight = 0;
  for(let i=1; i<height.length; i++) {
      maxLeft = Math.max(maxLeft, height[i-1]);
      maxLeftList[i] =  maxLeft;
  }
  for(let i=height.length-2; i>=0; i--) {
      maxRight = Math.max(maxRight, height[i+1]);
      maxRightList[i] =  maxRight;
  }
  for(const i in height) {
      const calculatedRes = (Math.min(maxLeftList[i], maxRightList[i])) - height[i];
      res += calculatedRes > 0 ? calculatedRes : 0;
  }
  return res;
};
*/

// Solution 2
var trap = function(height) {
  if(height.length == 0) return 0;
  let res = 0;
  let left = 0;
  let right = height.length - 1;
  let maxLeft = height[left];
  let maxRight = height[right];
  while(left < right) {
      if(height[left] < height[right]) {
          left++;
          maxLeft = Math.max(maxLeft, height[left]);
          res += maxLeft - height[left];
      } else {
          right--;
          maxRight = Math.max(maxRight, height[right]);
          res += maxRight - height[right];
      }
  }
  return res;
};

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));