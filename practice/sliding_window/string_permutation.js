function string_permutation(string1, string2) {

    if(string1.length > string2.length) return false;

    let count1 = {};
    let count2 = {};

    for(let i=0; i<string1.length; i++) {
        count1[string1[i]] = (1 + count1[string1[i]] || 1);
        count2[string2[i]] = (1 + count2[string2[i]] || 1);
    }

    if(checkHash(count1, count2)) return true;

    let left = 0;
    for(let right = string1.length; right < string2.length; right++) {
        count2[string2[right]] = (1 + count2[string2[right]] || 1);
        count2[string2[left]] -= 1;

        // if(count2[string2[left]] === 0) delete count2[string2[left]];
        left += 1;

        if(checkHash(count1, count2)) return true;

    }

    return false;

}

function checkHash(hash1, hash2) {
    for(const c in hash1) {
        if(!(c in hash2)) return false;
        if(hash1[c] !== hash2[c]) return false;
    }

    return true;
}

console.log(string_permutation('ab', 'bazbnmdboaloo'));