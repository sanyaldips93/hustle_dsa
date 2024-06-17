function valid_anagrams(string1, string2) {
    let hashMap = {};
    for(const char of string1) {
        if(hashMap[char]) {
            hashMap[char]++;
        } else {
            hashMap[char] = 1;
        }
    }

    for(const char of string2) {
        if(!hashMap[char]) {
            console.log('Not valid anagrams!');
            return;
        } else {
            hashMap[char]--;
        }
    }
    console.log('Valid anagrams!');
}

valid_anagrams('nigiri', 'nirigii');