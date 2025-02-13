var groupAnagrams = function(strs) {
  let map = {}

  for(let str of strs){
      let s = str.split('').sort().join('')
      if(!map[s]) map[s] = []
      map[s].push(str)
  }
  return Object.values(map)
};

var groupAnagrams = function(strs) {
  const hash = {};
  for(const string of strs) { // 0(n)
      const array = new Array(26).fill(0); // constant
      const ascii_differentiator = 'a'.charCodeAt(0); // constant
      for(char of string) { // 0(m)
          const ascii_diff = char.charCodeAt(0) - ascii_differentiator;
          array[ascii_diff] += 1;
      }
      if(hash[array]) {
          hash[array].push(string);
      } else {
          hash[array] = [string];
      }
  }
  const result = [];
  for(const key in hash) { // 0(n)
      result.push(hash[key]);
  }
  return result;
};