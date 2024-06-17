var longestConsecutive = function(nums) {
  const numsSet = new Set(nums);
  let longest = 0;
  for(const num of nums) {
      if(!numsSet.has(num-1)) {
          let length = 1;
          while(numsSet.has(num+length)) {
              length += 1;
          }
          longest = Math.max(longest, length);
      }
  }
  return longest;
};