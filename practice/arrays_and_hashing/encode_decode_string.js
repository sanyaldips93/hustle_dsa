function encode(array) {
    let res = "";
    for(const word of array) {
        const length = word.length;
        res += (length + "#" + word);
    }
    return decode(res);
}

function decode(str) {
    const res = [];
    let i = 0;

    while(i < str.length) {
        let j = i + 1;
        while(str[j] !== '#') {
            j += 1;
        }
        let length = parseInt(str.slice(i, j));
        res.push(str.slice(j+1, j+1+length));
        i = j + 1 + length;
    }

    return res;
}

console.log(encode(['rat', 'ate', 'a', 'cat']));