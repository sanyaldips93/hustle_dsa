/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
  const hash1 = {};
  const hash2 = {};
  for(let i=0; i<s.length; i++) {
      if(hash1[s[i]] && hash1[s[i]] !== t[i]){
          return false;
      }
      if(hash2[t[i]] && hash2[t[i]] !== s[i]){
        return false;
      }
      hash1[s[i]] = t[i];
      hash2[t[i]] = s[i];
  }
  return true;
};

console.log(isIsomorphic('badc', 'baba'));