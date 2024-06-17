var characterReplacement = function(s, k) {
  let res = 0;
  const count = {};
  let l = 0;
  let r = 0;
  while(r < s.length) {
      if(count[s[r]] !== undefined) count[s[r]] += 1;
      else count[s[r]] = 1;
      while((r-l+1) - Math.max(...getValues(count)) > k) {
          count[s[l]] -= 1;
          l += 1;
      }
      res = Math.max(res, (r-l+1));
      r += 1;
  }
  return res;
};

function getValues(hash) {
  const values = [];
  for (const key in hash) {
      values.push(hash[key]);
  }
  return values;
}

console.log(characterReplacement("AABABBA", 1));