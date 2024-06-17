var minEatingSpeed = function(piles, h) {
  let left = 0;
  let right = Math.max(...piles);;
  let res = right;

  while(left <= right) {
      const mid = Math.trunc((left+right)/2);
      let hours = 0;
      for(const num of piles) {
          hours += Math.ceil(num/mid);
      }

      if(hours > h) {
          left = mid + 1;
      } else if(hours <= h) {
          res = Math.min(res, mid);
          right = mid - 1;
      }
  }
  return res;
};

console.log(minEatingSpeed([45634], 45600));