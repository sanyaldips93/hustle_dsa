var lengthOfLongestSubstring = function(s) {
  let l = 0;
  let r = 0;
  let res = 0;
  let charSet = new Set();
  while(r < s.length) {
      while(charSet.has(s[r])) {
          charSet.delete(s[l]);
          l += 1;
      }
      charSet.add(s[r]);
      res = Math.max(res, r-l+1);
      r += 1;
  }
  return res;
};

console.log(lengthOfLongestSubstring('abcabcbb'));