var isValid = function(s) {
  const hash = {
      ')':'(',
      '}':'{',
      ']':'['
  };
  const temporaryArray = [];
  for(const char of s) {
      if(char === '(' || char === '{' || char === '[') {
          temporaryArray.push(char);
      } else {
          const bracket = temporaryArray.pop();
          if(bracket !== hash[char]) {
              return false;
          }
      }
  }

  if(temporaryArray.length > 0) {
      return false;
  }

  return true;
};

console.log(isValid("()"));