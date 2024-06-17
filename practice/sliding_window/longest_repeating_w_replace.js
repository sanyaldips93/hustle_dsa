function longest_repating(string, replace) {
    const count = {};
    let maxf = 0;
    let left = 0;
    let res = 0;

    for(let right = 0; right < string.length; right++) {
        count[string[right]] = 1 + count[string[right]] || 1;
        // maxf = Math.max(maxf, count[string[right]]); 

        while((right - left + 1) - Math.max(...Object.values(count)) > replace) { // or use maxf here.
            count[string[left]] -= 1;
            left++;
        }

        res = Math.max(res, (right - left + 1));
    }

    console.log(res);
}

longest_repating('BBCCBAB', 2);