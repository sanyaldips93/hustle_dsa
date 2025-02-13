var buyChoco = function(prices, money) {
  prices.sort((a,b) => a-b);
  if(money - prices[0] - prices[1] < 0) {
      return money;
  } else {
      return money - prices[0] - prices[1];
  }
};

console.log(buyChoco([1,2,2], 3));