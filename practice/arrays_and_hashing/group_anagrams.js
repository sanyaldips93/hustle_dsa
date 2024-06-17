function group_anagrams(array) {
    const hashMap = {}; // extra space
    for(const word of array) { // O(m)
        let array = new Array(26).fill(0); // constant
        const ascii_differentiator = 'a'.charCodeAt(0); // constant
        for(const char of word) { // O(n)
            const ascii_difference = char.charCodeAt(0) - ascii_differentiator; // constant
            array[ascii_difference] += 1;
        }
        if(hashMap[array]) {
            hashMap[array].push(word);
        } else {
            hashMap[array] = [word];
        }
    }
    return Object.values(hashMap);
}

console.log(group_anagrams(['eat', 'tea', 'ate', 'tan', 'ant', 'but']));