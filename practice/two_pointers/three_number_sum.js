function three_number_sum(array, target) {
    
    array.sort();
    const res = [];

    for(let idx=0; idx<array.length; idx++) {

        if(idx > 0 && array[idx] === array[idx - 1]) continue;
        const first_num = array[idx];
        let start = idx + 1;
        let end = array.length - 1;
        
        while(start < end) {
            const sum = first_num + array[start] + array[end];
            if(sum === target) {
                res.push([first_num, array[start], array[end]]);
                start++;
                while(array[start] === array[start - 1] && start < end) {
                    start++; // just need to update one pointer, the below logic will update another
                }
            }
            else if(sum < target) {
                start++;
            } else {
                end--;
            }
        }
    }

    return res;
}

console.log(three_number_sum([-3, 3, 0, 2, 1, -3, 2], 0));