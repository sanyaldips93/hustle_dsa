// Brute force

function container_w_most_water_bf(array) {
    let res = 0;
    for(let i=0; i<array.length; i++) {
        for(let j=i+1; j<array.length; j++) {
            const area = (j - i) * Math.min(array[i], array[j]);
            res = Math.max(res, area);
        }
    }
    console.log(res);
}

container_w_most_water_bf([1,2,7,3,5,6,4]);

// Linear time

function container_w_most_water(array) {
    let res = 0;
    let l = 0;
    let r = array.length - 1;
    while(l < r) {
        const area = (r - l) * Math.min(array[r], array[l]);
        res = Math.max(res, area);

        if(array[l] > array[r]) {
            r -= 1;
        } else {
            l += 1;
        }
    }
    console.log(res);
}

container_w_most_water([1,2,7,3,5,6,4]);