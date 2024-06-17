function top_k_frequent_elements(array, frequency) {
    const count = new Array(array.length + 1);
    const hashMap = {};
    const res = [];

    for(const element of array) { // 0(n)
        if(hashMap[element]) hashMap[element] += 1;
        else hashMap[element] = 1;
    }

    for(const ele in hashMap) { // 0(n)
        let count_val = hashMap[ele];
        let element = parseInt(ele);
        if(Array.isArray(count[count_val])) {
            count[count_val].push(element);
        } else {
            count[count_val] = [element];
        }
    }

    for(let i=count.length + 1; i>=0; i--) { // 0(n)
        if(Array.isArray(count[i])) {
            for(const element of count[i]) {
                res.push(element);
                if(res.length === frequency) {
                    return res;
                }
            }
        }
    }
}

console.log(top_k_frequent_elements([1,1,1,2,2,3,3,4], 2));