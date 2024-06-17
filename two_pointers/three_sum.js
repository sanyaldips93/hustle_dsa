var threeSum = function(nums) {
  const sortedNums = nums.sort((a,b) => a-b);
  console.log(sortedNums);
    const result = [];
    for(let i=0; i<sortedNums.length; i++) {
        if(i>0 && sortedNums[i] === sortedNums[i-1]) {
            continue;
        }
        let left = i+1;
        let right = sortedNums.length - 1;
        while(left < right) {
          let threeSum = sortedNums[left] + sortedNums[right] + sortedNums[i];
          if(threeSum > 0) right--;
          else if(threeSum < 0) left++;
          else {
              result.push([sortedNums[i], sortedNums[left], sortedNums[right]]);
              left++;
              while(sortedNums[left] === sortedNums[left-1] && left<right) {
                  left++;
              }
          }
        }
      }
  return result;
};

console.log(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))