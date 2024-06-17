var checkInclusion = function(s1, s2) {
  if(s1.length > s2.length) return false;
  const ar1 = new Array(26).fill(0);
  const ar2 = new Array(26).fill(0);
  for(const i in s1) {
      ar1[ord(s1[i]) - ord('a')] += 1;
      ar2[ord(s2[i]) - ord('a')] += 1;
  }
  let matches = 26;
  for(let i=0; i<26; i++) {
      if(ar1[i] !== ar2[i]) matches -= 1;
  }
  let l = 0;
  let r = s1.length;
  while(r < s2.length) {
      if(matches === 26) return true;
      let index = ord(s2[r]) - ord('a');
      ar2[index] += 1;
      if(ar2[index] === ar1[index]) {
          matches += 1;
      } else if(ar1[index] + 1 === ar2[index]) {
          matches -= 1;
      }

      let index2 = ord(s2[l]) - ord('a');
      ar2[index2] -= 1;
      if(ar2[index2] === ar1[index2]) {
        matches += 1;
      } else if(ar1[index2] - 1 === ar2[index2]) {
        matches -= 1;
      }
      l += 1;
      r += 1;
  }
  return matches === 26;
};

function ord(char) {
  return char.charCodeAt(0);
}

console.log(checkInclusion('ad', 'ooodcaoo'));