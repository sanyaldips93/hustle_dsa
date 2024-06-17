function encodeAndDecodeString(strings) {
  function encode(strings) {
    let res = '';
    for(const word of strings) {
      res += word.length + '#' + word;
    }
    return res;
  }
  const encodedString = encode(strings);
  function decode(encodedString) {
    const res = [];
    let i = 0;
    while(i < encodedString.length) {
      let j=i;
      while(encodedString[j] !== '#') {
        j++;
      }
      const strLength = encodedString.slice(i, j);
      const word = encodedString.slice(j+1, j+1+parseInt(strLength));
      res.push(word);
      i = j+1+parseInt(strLength);
    }
    return res;
  }
  const decodedString = decode(encodedString);
  console.log(strings, decodedString);
}

encodeAndDecodeString(['ne#t', 'cod#']);

