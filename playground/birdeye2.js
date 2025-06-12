// const cache = createCache();

// cache.set('key1', 'value1', 3000); /


function createCache() {
  
  const len = 3;
  const hash = {};

  function get(key) {
    const res = hash[key];
    if (res == null) {
      return null;
    }
    [val, exp, time] = res;
    if (exp == null) {
      return val;
    }

    const curtime = Date.now()
    const diff = curtime - time;
    if (diff > exp) {
      delete hash[key];
      return null;
    }
    return val;
  }

  function set(key, val, exp=null) {
    if(key in hash) {
      if (exp == null) {
        if (hash[key].length == 3) { // we will have to check if hash[key] is an array
          hash[key][0] = val;
        } else {
          hash[key] = [val];
        }
      } else {
        hash[key] = [val, exp, Date.now()];
      }
    }
    else {
      if(exp == null) {
        hash[key] = [val];
      } else {
        hash[key] = [val, exp, Date.now()];
      }
    }
    return 'OK';
  }

  function getHash() {
    return hash;
  }

  return {get, set, getHash};
}


// const cache1 = createCache();
// cache1.set('key1', 'value1', 3000); 
// console.log(cache1.get('key1'));
// setTimeout(() => {
//   console.log(cache1.get('key1'));
// }, 3500);

const cache = createCache();
cache.set('key1', 'value1', 3000);
// cache.set('key1', 'value3', 5000);
setTimeout(() => {
  console.log(cache.get('key1'));
}, 3500);

setTimeout(() => {
  cache.set('key2', 'value2', 5000);
}, 1000);
setTimeout(() => {
  console.log(cache.get('key2')); 
}, 4000);
setTimeout(() => {
  console.log(cache.getHash()); 
}, 6000);