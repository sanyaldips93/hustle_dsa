var twoSum = function(numbers, target) {
  let a = 0;
  let b = numbers.length - 1;
  while(a<b) {
      let sum = numbers[a] + numbers[b];
      if(sum === target) {
          return [a+1,b+1];
      }
      if(sum > target) b--;
      if(sum < target) a++;
  }
};