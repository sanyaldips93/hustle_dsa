function contains_duplicate(array) {
    const length = array.length;
    const hashmap = {};
    for(const element of array) {
        if(hashmap[element]) {
            console.log('Duplicate number is present ->, ', element);
        } else {
            hashmap[element] = true;
        }
    }
    console.log('No duplicate numbers present!');
}

contains_duplicate([1,2,3,1]);