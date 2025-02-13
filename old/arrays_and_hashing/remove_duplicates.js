var removeDuplicates = function(nums) {
  const hashMap = {};
  for(const num of nums) {
      if(Array.isArray(hashMap[0])) {
          if(hashMap[0].includes(num)) continue;
          else hashMap[0].push(num);
      } else {
          hashMap[0] = [num];
      }
  }
  let i = 0;
  for(element of hashMap[0]) {
      nums[i] = element;
      i++;
  }
  const count = i;
  while(i<nums.length) {
      nums[i] = '_';
      i++;
  }
  return count;
};