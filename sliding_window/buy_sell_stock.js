// T - O(n), M - O(1)
var maxProfit = function(prices) {
  let l = 0;
  let r = 1;
  let max = 0;
  while(r < prices.length) {
      if(prices[l] < prices[r]) {
          const profit = prices[r] - prices[l]
          max = Math.max(profit, max);
      } else {
          l = r;
      }
      r += 1;
  }
  return max;
};