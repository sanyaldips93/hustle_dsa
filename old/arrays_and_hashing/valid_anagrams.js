function valid_anagrams(string1, string2) {
  if(string1.length !== string2.length) return false;
  const hash = {}; //initialising the hash
  for(const char of string1) {
    if(hash[char]) {
      hash[char]++;
    } else {
      hash[char] = 1; // if we are observing the char for the first time, we set a value of 1.
    }
  }

  // we will check the other string's chars in the hashmap
  for(const char of string2) {
    if(!hash[char]) {
      console.log('Not valid anagrams!');
      return;
    } else {
      hash[char]--; // we will decrement count of the char key in hash if we observe it in the string and the hash.
    }
  }
  console.log('Valid anagrams!');
  return;
}

valid_anagrams('ab', 'b');