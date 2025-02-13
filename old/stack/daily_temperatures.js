// Time - O(n), Memory - O(n)
var dailyTemperatures = function(tempS) {
  const res = new Array(tempS.length).fill(0);
  const stack = [];
  for(const idx in tempS) {
      const temp = tempS[idx];
      while(stack.length && temp > stack[stack.length - 1][0]) {
          const [lastTemp, lastIndex] = stack.pop();
          res[lastIndex] = idx - lastIndex;
      }
      stack.push([temp, idx]);
  }
  return res;
};

console.log(dailyTemperatures([73,74,75,71,69,72,76,73]));