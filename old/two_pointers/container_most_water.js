// Solution 1 - O(n^2) - TLE
/*
var maxArea = function(height) {
  let maxArea = 1;
  for(let i=0; i<height.length; i++) {
      for(let j=i+1; j<height.length; j++) {
          const minHeight = Math.min(height[i], height[j]);
          const diffInIdx = j-i;
          const area =  minHeight * diffInIdx;
          maxArea = Math.max(maxArea, area);
      }
  }
  return maxArea;
};
*/

// Solution 2 - O(n)
var maxArea = function(height) {
  let left = 0;
  let right = height.length - 1;
  let maxArea = 0;
  while(left < right) {
      const minHeight = Math.min(height[left], height[right]);
      const diffInIdx = right - left;
      const area =  minHeight * diffInIdx;
      maxArea = Math.max(maxArea, area);
      if(height[left] > height[right]) {
          right--;
      } else {
          left++;
      }
  }
  return maxArea;
};

console.log(maxArea([0,2]));