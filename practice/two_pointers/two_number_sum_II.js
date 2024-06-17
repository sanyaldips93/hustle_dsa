function two_number_sum(array, target) {
    let startIdx = 0;
    let endIdx = array.length - 1;
    
    while(startIdx < endIdx) {
        const sum = array[startIdx] + array[endIdx];
        if(sum === target) return [startIdx+1, endIdx+1];
        else if(sum < target) startIdx++;
        else endIdx--;
    }

    return [];
}

console.log(two_number_sum([1,3,4,5,7,11], 9));