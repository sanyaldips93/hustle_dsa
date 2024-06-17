function longest_sequence(array) {
    let nums = new Set(array);
    let longest = 0;
    
    for(const num of array) {
        
        if(!(nums.has(num-1))) {
            
            let length = 1;
            while(nums.has(num+length)) {
                length += 1;
            }
            longest = Math.max(longest, length);
        }
    }

    console.log(longest);
}

longest_sequence([100, 1, 2, 200, 3, 4]);