var topKFrequent = function(nums, k) {
  const count = new Array(nums.length + 1).fill(0);
  const hash = {};
  const res = [];
  for(const number of nums) { // 0(n)
      if(hash[number]) hash[number]++;
      else hash[number] = 1;
  }

  for(const ele in hash) { // 0(n)
      let count_val = hash[ele];
      let element = parseInt(ele);
      if(Array.isArray(count[count_val])) {
          count[count_val].push(element);
      } else {
          count[count_val] = [element];
      }
  }

  for(let i=count.length+1; i>=0; i--) { //0 (n)
      if(Array.isArray(count[i])) {
          for(const ele of count[i]) { 
              res.push(ele);
              if(res.length === k) return res;
          }
      }
  }
};

topKFrequent([1,1,1,2,3,3], 2);