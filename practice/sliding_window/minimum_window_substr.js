function minimum_substr(str1, str2) {

    const count = {};
    const window = {};

    for(const char of str2) {
        count[char] = 1 + count[char] || 1;
    }

    let have = 0;
    const need = str2.length;

    let res = [-1, -1];
    let resVal = Infinity;

    let left = 0;

    for(let right = 0; right < str1.length; right++) {
        window[str1[right]] = 1 + window[str1[right]] || 1;
        if(str1[right] in count && window[str1[right]] === count[str1[right]]) {
            have += 1;
        }

        while(have === need) {
            if(right - left + 1 < resVal) {    
                res = [left, right];
                resVal = right - left + 1;
            }
            window[str1[left]] -= 1;

            if(str1[left] in count && window[str1[left]] < count[str1[left]]) {
                have -= 1;
            }
            left += 1;
        }
    }
    const [l, r] = res;
    return resVal != Infinity ? str1.slice(l, r+1) : "";
}

console.log(minimum_substr('avscobikbanfcf', 'abc'));