var search = function(nums, target) {
  let l = 0;
  let r = nums.length - 1;
  while(l <= r) {
      let m = Math.trunc((l+r)/2);
      if(target === nums[m]) {
          return m;
      }
      if(nums[l] <= nums[m]) {
          if(target < nums[m] || target < nums[l]) {
              l = m+1;
          } else {
              r = m-1;
          }
      } else {
          if(target > nums[m] || target > nums[r]) {
              r = m-1;
          } else { 
              l = m+1;
          }
      }
  }
  return -1;
};

console.log(search([4,5,6,7,8,1,2,3], 8));