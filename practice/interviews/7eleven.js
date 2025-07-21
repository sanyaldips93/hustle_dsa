// Remove duplicates but keep the last occurrence of each character

// console.log(removeDuplicatesKeepLast("abcaccb"));   // Output: "acb"
// console.log(removeDuplicatesKeepLast("aabbcc"));   // Output: "abc"
// console.log(removeDuplicatesKeepLast("cbacdcbc")); // Output: "adbc"


// 'abcaccb' - 
// 'bca' - 'acb'


function removeDuplicatesKeepLast(str) {
  const length = length(str)
  hash = {}
  const res = ""
  for (let i=length-1; i>=0; i--) {
    if (!hash.contains(str[i])) {
      hash.add(str[i])
      res += str[i]
    }
  }
  const res2 = ""
  for(i=length(res); i>=0; i--){
    res2 += res[i]
  }
  return res2;
}


// in below code snippet, implement `sleep` function such that the flow after `Start` pauses for N Milliseconds (1000 in below code) & then `End` should be displayed
 
async function sleep(ms) {
    setTimeout(() => {
      console.log('Inside settimeout');
    }, ms);
}
 
async function flow() {
  console.log("Start"); // stack will print
  await sleep(1000); // stack will push to webapi -> microtask q -> stack will print
  console.log("End"); // stack will print
}

flow().then().catch();