var isPalindrome = function(s) {
  let trimmedLowerCaseAlphaNumericStr = '';
  let lowerCasedStringArr = s.toLowerCase().split('');
  for(const char of lowerCasedStringArr) {
      if((char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122) || (char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57)) {
          trimmedLowerCaseAlphaNumericStr += char;
      }
  }
  let a = 0;
  let b = trimmedLowerCaseAlphaNumericStr.length - 1;
  while(a<=b) {
      if(trimmedLowerCaseAlphaNumericStr[a] !== trimmedLowerCaseAlphaNumericStr[b]) {
          return false;
      }
      a++;
      b--;
  }
  return true;
};

/*
Solution 2
var isPalindrome = function(s) {
    let newStr = s.toLowerCase().replace(/[^0-9a-z]/g, "");
    let left = 0, right = newStr.length-1;
    
    while(left < right){
        if(newStr[left] !== newStr[right]) return false
        left++
        right--
    }
    return true
};
*/

console.log(isPalindrome("0P"));