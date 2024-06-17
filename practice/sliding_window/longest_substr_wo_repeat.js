function longest_substr(string) {
    
    let res = 0;
    const strSet = new Set();
    let left = 0;
    let right = 0;

    while(right < string.length) {
        while(strSet.has(string[right])) {
            strSet.delete(string[left]);
            left += 1;
        }

        res = Math.max(res, right - left + 1);
        strSet.add(string[right]);
        right++;

    }

    console.log(res);
}

longest_substr('abbccadab');