var frequencySort = function(nums) {
  nums.sort((a,b) => a-b);
  const arr = new Array(nums[nums.length-1]).fill(0);
  const hash = {};
  let res = [];
  for(const num of nums) {
      if(!hash[num]) hash[num] = 1;
      else hash[num]++;
  }
  for(const key in hash) {
    if(Array.isArray(arr[hash[key]])) {
      arr[hash[key]].push(...new Array(hash[key]).fill(Number(key)));
    } else {
      arr[hash[key]] = new Array(hash[key]).fill(Number(key));
    }
  }
  for(let i=0; i<arr.length; i++) {
      if(Array.isArray(arr[i])) {
          res.push(...arr[i]);
      }
  }
  return res;
};

console.log(frequencySort([2,3,1,3,2]));