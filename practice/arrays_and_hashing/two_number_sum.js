function two_number_sum(array, number) {
    const hashMap = {};
    for(const idx in array) {
        const element = array[idx];
        const target = number - element;
        if(hashMap[target]) {
            return [hashMap[target], idx];
        } else {
            hashMap[element] = idx;
        }
    }
    return [];
}

console.log(two_number_sum([3,6,4,8], 11));